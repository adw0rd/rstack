"""Контракт каталога: полнота, воспроизводимость, локальные refs, защита core."""

import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "generator" / "generate.py"


class CatalogTest(unittest.TestCase):
    def generate(self, target, *extra):
        return subprocess.run(
            [sys.executable, str(GENERATOR), "--output", str(target), *extra],
            capture_output=True, text=True, check=False,
        )

    def test_generate_complete_compact_catalog_and_local_refs(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            result = self.generate(output)
            self.assertEqual(result.returncode, 0, result.stderr)
            inventory = json.loads((ROOT / "inventory.json").read_text())
            self.assertEqual(len(inventory["skills"]), 61)
            expected = ({x["skill"] for x in inventory["skills"]} - {"review", "qa", "investigate"}) | set(inventory["aliases"])
            actual = {p.parent.name for p in (output / "skills").glob("*/SKILL.md")}
            self.assertEqual(actual, expected)
            self.assertEqual(len(actual), 59)  # 58 процедур и один реальный alias.
            for entry in (output / "skills").glob("*/SKILL.md"):
                content = entry.read_text()
                self.assertLessEqual(len(entry.read_bytes()), 8192, entry)
                self.assertTrue(content.startswith("---\nname: " + entry.parent.name + "\n"))
                self.assertRegex(content, r"(?m)^description: .+")
                self.assertNotRegex(content, r"TODO(?:\s*[:\[]|\s+replace)")
                self.assertNotIn("hookSpecificOutput", content)
                for ref in re.findall(r"\]\(([^)]+)\)", content):
                    self.assertNotIn("..", Path(ref).parts)
                    resolved = (entry.parent / ref).resolve()
                    self.assertTrue(resolved.is_relative_to(entry.parent.resolve()))
                    self.assertTrue(resolved.is_file(), (entry, ref))

    def test_deterministic_and_check_detects_drift(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            self.assertEqual(self.generate(first).returncode, 0)
            self.assertEqual(self.generate(second).returncode, 0)
            def snapshot(root):
                return {str(p.relative_to(root)): p.read_bytes() for p in Path(root).rglob("*") if p.is_file()}
            self.assertEqual(snapshot(Path(first)), snapshot(Path(second)))
            self.assertEqual(self.generate(first, "--check").returncode, 0)
            entry = Path(first) / "skills" / "browse" / "SKILL.md"
            entry.write_text(entry.read_text() + "\nmanual edit\n")
            self.assertNotEqual(self.generate(first, "--check").returncode, 0)
            self.assertIn("manual edit", entry.read_text())

    def test_preserves_existing_core_and_refuses_overwrite_or_symlink(self):
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            output = Path(temp)
            core = output / "skills" / "review" / "SKILL.md"
            core.parent.mkdir(parents=True)
            core.write_text("Qwen core sentinel\n")
            self.assertEqual(self.generate(output).returncode, 0)
            self.assertEqual(core.read_text(), "Qwen core sentinel\n")
            target = output / "skills" / "browse" / "SKILL.md"
            target.write_text("user edit\n")
            self.assertNotEqual(self.generate(output).returncode, 0)
            self.assertEqual(target.read_text(), "user edit\n")
            target.unlink()
            target.symlink_to(Path(outside) / "sentinel")
            self.assertNotEqual(self.generate(output).returncode, 0)
            self.assertFalse((Path(outside) / "sentinel").exists())

    def test_every_generated_entry_inlines_its_source_checks(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            result = self.generate(output)
            self.assertEqual(result.returncode, 0, result.stderr)
            spec = importlib.util.spec_from_file_location(
                "rstack_workflows_inline_checks", ROOT / "generator" / "workflows.py"
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            inventory = json.loads((ROOT / "inventory.json").read_text())
            aliases = inventory["aliases"]
            entries = sorted((output / "skills").glob("*/SKILL.md"))
            self.assertEqual(len(entries), 59)
            failures = []
            for entry in entries:
                name = entry.parent.name
                canonical = aliases.get(name, name)
                expected = "\n".join("- " + check for check in module.WORKFLOWS[canonical]["checks"])
                content = entry.read_text()
                header = "## Обязательный чеклист результата\n\n"
                if header not in content:
                    failures.append(name + ": inline checklist is missing")
                else:
                    actual = content.split(header, 1)[1].split("\n\n## Материалы", 1)[0].strip()
                    if actual != expected:
                        failures.append(name + ": inline checks differ from source")
                if "Перед отчётом проверь [критерии и сценарии]" in content:
                    failures.append(name + ": acceptance reference remains mandatory")
                if "развёрнутые критерии и сценарии" not in content or "дополнительная справка" not in content:
                    failures.append(name + ": expanded acceptance is not marked optional")
            self.assertEqual(failures, [])

    def test_capabilities_have_specific_preconditions(self):
        spec = importlib.util.spec_from_file_location("rstack_workflows", ROOT / "generator" / "workflows.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        data = module.WORKFLOWS
        for name in ["browse", "ios-qa", "ios-sync", "pair-agent", "benchmark-models", "sync-gbrain"]:
            workflow = data[name]
            self.assertTrue(workflow["prerequisites"], name)
            self.assertNotEqual(workflow["capability"], "native", name)
            self.assertGreaterEqual(len(workflow["steps"]), 5, name)
        self.assertNotEqual(data["ios-qa"]["steps"], data["ios-sync"]["steps"])
        self.assertNotEqual(data["browse"]["steps"], data["pair-agent"]["steps"])

    def test_rcode_0_10_runtime_guidance_and_core_alignment(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            self.assertEqual(self.generate(output).returncode, 0)
            spec = importlib.util.spec_from_file_location(
                "rstack_workflows_runtime", ROOT / "generator" / "workflows.py"
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            inventory = json.loads((ROOT / "inventory.json").read_text())
            aliases = inventory["aliases"]
            generated_entries = sorted((output / "skills").glob("*/SKILL.md"))
            core_entries = [ROOT / "skills" / name / "SKILL.md" for name in ("review", "qa", "investigate")]
            self.assertEqual(len(generated_entries), 59)
            for entry in [*generated_entries, *core_entries]:
                text = entry.read_text()
                self.assertLessEqual(len(entry.read_bytes()), 8192, entry)
                self.assertIn("ask_user", text, entry)
                self.assertIn("read_memory", text, entry)
                self.assertIn("write_memory", text, entry)
                self.assertIn("--sandbox", text, entry)
                self.assertIn("--sandbox read-only", text, entry)
                self.assertIn("TMPDIR", text, entry)
                self.assertIn("explorer`/`reviewer`/`worker", text, entry)
                self.assertIn("интерактивному основному агенту вне `/plan`", text, entry)
                self.assertIn("127.0.0.1", text, entry)
                self.assertNotIn("В `/plan` и read-only не вызывай shell", text, entry)
                self.assertNotIn("вопросы пользователю задавай обычным текстом", text, entry)
                self.assertNotIn("Вопрос пользователю задай текстом", text, entry)
                self.assertNotIn("спроси пользователя обычным текстом", text, entry)
                for line in text.splitlines():
                    if re.match(r"^(?:\d+\.|-)\s", line):
                        self.assertEqual(line.count("`") % 2, 0, (entry, line))
            for entry in generated_entries:
                name = entry.parent.name
                canonical = aliases.get(name, name)
                text = entry.read_text()
                steps_block = text.split("## Порядок работы\n\n", 1)[1].split("\n\n## Обязательный чеклист", 1)[0]
                step_lines = steps_block.splitlines()
                self.assertEqual(len(step_lines), len(module.WORKFLOWS[canonical]["steps"]), name)
                for index, line in enumerate(step_lines, 1):
                    self.assertTrue(line.startswith(f"{index}. "), (name, line))
            eng_text = (output / "skills" / "plan-eng-review" / "SKILL.md").read_text()
            self.assertIn("исключи побочные эффекты вне пробы", eng_text)
            learn_text = (output / "skills" / "learn" / "SKILL.md").read_text()
            self.assertEqual(len(module.WORKFLOWS["learn"]["steps"]), 6)
            self.assertIn("чтение через `read_memory` по `id`", learn_text)
            self.assertIn("запись через `write_memory` со `scope` `project` или `global`", learn_text)


if __name__ == "__main__":
    unittest.main()
