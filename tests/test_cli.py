import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CLI = Path(__file__).resolve().parents[1] / 'bin' / 'rstack'


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='rstack-tests-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'project'
        self.root.mkdir()
        self.env = {'PATH': os.environ.get('PATH', ''), 'HOME': self.temp.name,
                    'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull}
        self.git('init', '-q', '-b', 'main')
        self.git('config', 'user.name', 'Runtime Fixture')
        self.git('config', 'user.email', 'runtime@example.invalid')
        self.write('README.md', 'Project fixture\n')
        self.write('source.py', 'def total(values):\n    return sum(values)\n')
        self.write('.gitignore', 'ignored.txt\ninternal/\n')
        self.git('add', '.')
        self.git('commit', '-q', '-m', 'Initial fixture')

    def git(self, *args, **kwargs):
        return subprocess.run(['git', '-C', str(self.root), *args], env=self.env,
                              check=True, capture_output=True, **kwargs)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def cli(self, *args, expected=0):
        result = subprocess.run([sys.executable, str(CLI), *args], env=self.env,
                                capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        self.assertEqual(result.stderr, '')
        return json.loads(result.stdout)

    def test_context_covers_staged_unstaged_untracked_and_excludes_ignored_secrets(self):
        self.write('source.py', 'def total(values):\n    return sum(values) + 1\n')
        self.git('add', 'source.py')
        self.write('source.py', 'def total(values):\n    return sum(values) + 2\n')
        self.write('new file.py', 'value = 7\n')
        self.write('ignored.txt', 'IGNORED_SECRET\n')
        self.write('.env', 'API_KEY=ENV_SECRET\n')
        first = self.cli('context', '--root', str(self.root))
        paths = {entry['path'] for entry in first['files']}
        self.assertEqual(paths, {'source.py', 'new file.py'})
        self.assertNotIn('IGNORED_SECRET', json.dumps(first))
        self.assertNotIn('ENV_SECRET', json.dumps(first))
        self.write('ignored.txt', 'OTHER_IGNORED_SECRET\n')
        self.write('.env', 'API_KEY=OTHER_ENV_SECRET\n')
        second = self.cli('context', '--root', str(self.root))
        self.assertEqual(first['snapshot'], second['snapshot'])
        self.write('new file.py', 'value = 8\n')
        third = self.cli('context', '--root', str(self.root))
        self.assertNotEqual(first['snapshot'], third['snapshot'])

    def test_context_does_not_follow_symlinks_or_read_tracked_ignored_files(self):
        outside = Path(self.temp.name) / 'outside.txt'
        outside.write_text('OUTSIDE_SECRET')
        (self.root / 'linked.txt').symlink_to(outside)
        self.write('ignored.txt', 'TRACKED_IGNORED_SECRET')
        self.git('add', '-f', 'ignored.txt')
        result = self.cli('context', '--root', str(self.root))
        self.assertEqual(result['files'], [])
        reasons = {entry['reason'] for entry in result['omitted']}
        self.assertIn('ignored', reasons)
        self.assertIn('symlink', reasons)

    def test_directory_replaced_by_file_keeps_deleted_children_in_context_and_diff(self):
        self.write('node/child.txt', 'old child\n')
        self.git('add', 'node/child.txt')
        self.git('commit', '-q', '-m', 'Add nested fixture')
        (self.root / 'node/child.txt').unlink()
        (self.root / 'node').rmdir()
        self.write('node', 'replacement file\n')
        context = self.cli('context', '--root', str(self.root))
        files = {entry['path']: entry for entry in context['files']}
        self.assertTrue(files['node/child.txt']['deleted'])
        self.assertIn('node', files)
        diff = self.cli('diff', '--root', str(self.root))
        self.assertIn('-old child', diff['diff'])
        self.assertIn('+replacement file', diff['diff'])
        self.assertFalse(diff['truncated'])

    def test_context_disables_repository_and_user_fsmonitor_hooks(self):
        trap = self.write('fsmonitor-trap.sh', '#!/bin/sh\nprintf bad > fsmonitor-ran\n')
        trap.chmod(0o700)
        self.git('config', 'core.fsmonitor', str(trap))
        (Path(self.temp.name) / '.gitconfig').write_text('[core]\nfsmonitor = ' + str(trap) + '\n')
        self.cli('context', '--root', str(self.root))
        self.assertFalse((self.root / 'fsmonitor-ran').exists())

    def test_context_and_diff_refuse_configured_clean_filters_without_running_them(self):
        trap = self.write('clean-trap.sh', '#!/bin/sh\nprintf bad > clean-filter-ran\ncat\n')
        trap.chmod(0o700)
        self.write('.gitattributes', 'source.py filter=trap\n')
        self.write('source.py', 'def total(values):\n    return sum(values) + 1\n')
        self.git('config', 'filter.trap.clean', str(trap))
        for command in ('context', 'diff'):
            with self.subTest(command=command):
                result = self.cli(command, '--root', str(self.root), expected=2)
                self.assertEqual(result['error'], 'unsupported_git_filter')
                self.assertFalse((self.root / 'clean-filter-ran').exists())

    def test_base_includes_committed_changes_on_a_clean_tree(self):
        self.write('source.py', 'def total(values):\n    return sum(values) + 1\n')
        self.git('add', 'source.py')
        self.git('commit', '-q', '-m', 'Change fixture behavior')
        result = self.cli('diff', '--root', str(self.root), '--base', 'HEAD~1')
        self.assertIn('+    return sum(values) + 1', result['diff'])
        self.assertEqual(result['paths'], ['source.py'])

    def test_staged_rename_diff_includes_deleted_source(self):
        self.git('mv', 'source.py', 'renamed.py')
        result = self.cli('diff', '--root', str(self.root))
        self.assertEqual(set(result['paths']), {'source.py', 'renamed.py'})
        self.assertIn('--- a/source.py\n+++ /dev/null', result['diff'])
        self.assertIn('--- /dev/null\n+++ b/renamed.py', result['diff'])
        self.assertFalse(result['truncated'])
        source = self.cli('diff', '--root', str(self.root), '--path', 'source.py')
        self.assertEqual(source['paths'], ['source.py'])
        self.assertIn('-def total(values):', source['diff'])

    def test_committed_rename_from_base_includes_deleted_source(self):
        self.git('switch', '-q', '-c', 'rename-feature')
        self.git('mv', 'source.py', 'renamed.py')
        self.git('commit', '-q', '-m', 'Rename fixture source')
        context = self.cli('context', '--root', str(self.root), '--base', 'main')
        files = {entry['path']: entry for entry in context['files']}
        self.assertEqual(set(files), {'source.py', 'renamed.py'})
        self.assertTrue(files['source.py']['deleted'])
        result = self.cli('diff', '--root', str(self.root), '--base', 'main')
        self.assertEqual(set(result['paths']), {'source.py', 'renamed.py'})
        self.assertIn('--- a/source.py\n+++ /dev/null', result['diff'])
        self.assertIn('--- /dev/null\n+++ b/renamed.py', result['diff'])
        self.assertFalse(result['truncated'])

    def test_diff_includes_untracked_and_literal_weird_names_without_external_drivers(self):
        self.write('source.py', 'def total(values):\n    return sum(values) + 1\n')
        self.write('-x [draft].py', 'literal = 9\n')
        trap = self.write('external-diff.sh', '#!/bin/sh\nprintf bad > trap-ran\n')
        trap.chmod(0o700)
        self.write('.gitattributes', '*.py diff=trap\n')
        self.git('config', 'diff.external', str(trap))
        self.git('config', 'diff.trap.textconv', str(trap))
        result = self.cli('diff', '--root', str(self.root), '--path', '-x [draft].py')
        self.assertIn('+literal = 9', result['diff'])
        self.assertEqual(result['paths'], ['-x [draft].py'])
        complete = self.cli('diff', '--root', str(self.root))
        self.assertIn('+    return sum(values) + 1', complete['diff'])
        self.assertFalse((self.root / 'trap-ran').exists())

    def test_diff_bounds_output_and_rejects_escape_invalid_and_option_refs(self):
        self.write('large.txt', 'long line ' * 4000)
        result = self.cli('diff', '--root', str(self.root), '--max-bytes', '300')
        self.assertTrue(result['truncated'])
        self.assertLessEqual(len(result['diff'].encode()), 300)
        for reference in ['does-not-exist', '--output=/tmp/nope']:
            result = self.cli('context', '--root', str(self.root), '--base=' + reference, expected=2)
            self.assertEqual(result['error'], 'invalid_base')
        result = self.cli('diff', '--root', str(self.root), '--path', '../outside.txt', expected=2)
        self.assertEqual(result['error'], 'invalid_path')

    def test_checks_discovers_without_executing_package_scripts(self):
        self.write('Cargo.toml', '[package]\nname="fixture"\nversion="0.1.0"\n')
        self.write('pyproject.toml', '[tool.pytest.ini_options]\ntestpaths=["tests"]\n')
        self.write('package.json', json.dumps({'scripts': {
            'test': 'printf bad > trap-ran', 'lint': 'eslint .', 'postinstall': 'printf bad > install-ran'}}))
        result = self.cli('checks', '--root', str(self.root))
        argv = [check['argv'] for check in result['checks']]
        self.assertIn(['cargo', 'test', '--all-targets'], argv)
        self.assertIn(['python3', '-m', 'pytest'], argv)
        self.assertIn(['npm', 'run', 'test'], argv)
        self.assertIn(['npm', 'run', 'lint'], argv)
        self.assertFalse(any('postinstall' in words for words in argv))
        self.assertFalse((self.root / 'trap-ran').exists())
        self.assertFalse((self.root / 'install-ran').exists())

    def test_invalid_metadata_returns_json_without_a_traceback(self):
        self.write('package.json', '[]')
        result = self.cli('checks', '--root', str(self.root), expected=2)
        self.assertEqual(result['error'], 'invalid_metadata')

    def test_unittest_discovery_is_not_confused_with_pytest(self):
        self.write('tests/test_total.py', 'import unittest\n')
        result = self.cli('checks', '--root', str(self.root))
        self.assertIn(['python3', '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                      [check['argv'] for check in result['checks']])

    def test_report_rejects_false_pass_and_stale_snapshot_without_writing(self):
        report = self.root / 'findings.json'
        report.write_text(json.dumps({'skill': 'review', 'status': 'pass', 'findings': [
            {'severity': 'P1', 'path': 'source.py', 'line': 2, 'message': 'Incorrect result'}], 'checks': []}))
        result = self.cli('report', '--root', str(self.root), '--input', str(report), expected=2)
        self.assertEqual(result['error'], 'contradictory_report')
        report.write_text(json.dumps({'skill': 'qa', 'status': 'pass', 'findings': [], 'checks': [
            {'argv': ['python3', '-m', 'unittest'], 'exit_code': 1, 'result': 'fail'}]}))
        result = self.cli('report', '--root', str(self.root), '--input', str(report), expected=2)
        self.assertEqual(result['error'], 'contradictory_report')
        report.write_text(json.dumps({'skill': 'qa', 'status': 'pass', 'findings': [], 'checks': [
            {'argv': ['python3', '-m', 'unittest'], 'exit_code': None, 'result': 'not_run'}]}))
        result = self.cli('report', '--root', str(self.root), '--input', str(report), expected=2)
        self.assertEqual(result['error'], 'contradictory_report')
        report.write_text(json.dumps({'skill': 'review', 'status': 'partial', 'findings': [],
                                     'checks': [], 'snapshot': '0' * 64}))
        result = self.cli('report', '--root', str(self.root), '--input', str(report), expected=2)
        self.assertEqual(result['error'], 'stale_snapshot')
        self.assertFalse((self.root / '.rstack').exists())

    def test_valid_report_is_caller_reported_and_keeps_coverage_limits(self):
        report = self.root / 'findings.json'
        report.write_text(json.dumps({'skill': 'review', 'status': 'partial', 'findings': [],
                                     'checks': [], 'coverage_gaps': ['Live API not exercised']}))
        result = self.cli('report', '--root', str(self.root), '--input', str(report))
        self.assertEqual(result['assessment_kind'], 'caller_reported')
        self.assertEqual(result['coverage_gaps'], ['Live API not exercised'])
        self.assertEqual(result['status'], 'partial')

    def test_report_uses_the_same_explicit_base_as_context(self):
        self.write('source.py', 'def total(values):\n    return sum(values) + 1\n')
        self.git('add', 'source.py')
        self.git('commit', '-q', '-m', 'Change fixture')
        context = self.cli('context', '--root', str(self.root), '--base', 'HEAD~1')
        report = Path(self.temp.name) / 'report.json'
        report.write_text(json.dumps({'skill': 'review', 'status': 'issues',
                                     'snapshot': context['snapshot'], 'findings': [
            {'severity': 'P2', 'path': 'source.py', 'line': 2, 'message': 'Incorrect sum'}]}))
        result = self.cli('report', '--root', str(self.root), '--base', 'HEAD~1', '--input', str(report))
        self.assertEqual(result['snapshot'], context['snapshot'])
        self.assertEqual(result['base'], context['base'])

    def test_validate_checks_reference_style_resource_links(self):
        skills = Path(self.temp.name) / 'skills'
        skill = skills / 'review'
        (skill / 'references').mkdir(parents=True)
        (skill / 'references/checklist.md').write_text('Check behavior.\n')
        prefix = '---\nname: review\ndescription: Review changes.\n---\nRead [checklist][resource].\n'
        (skill / 'SKILL.md').write_text(prefix + '[resource]: references/checklist.md\n')
        self.assertTrue(self.cli('validate', '--skills', str(skills))['valid'])
        (skill / 'SKILL.md').write_text(prefix + '[resource]: ../../outside.md\n')
        result = self.cli('validate', '--skills', str(skills), expected=2)
        self.assertIn('outside_skill', [error['error'] for error in result['errors']])

    def test_validate_checks_local_resource_boundaries_and_metadata(self):
        skills = Path(self.temp.name) / 'skills'
        skill = skills / 'review'
        (skill / 'references').mkdir(parents=True)
        (skill / 'SKILL.md').write_text('---\nname: review\ndescription: Review code changes when requested.\n---\nRead [checklist](references/checklist.md).\n')
        (skill / 'references/checklist.md').write_text('Check behavior.\n')
        result = self.cli('validate', '--skills', str(skills))
        self.assertEqual(result['skills'], ['review'])
        self.assertTrue(result['valid'])
        (skill / 'SKILL.md').write_text('---\nname: review\ndescription: Review code changes when requested.\n---\nRead [outside](../common.md).\n')
        result = self.cli('validate', '--skills', str(skills), expected=2)
        self.assertFalse(result['valid'])
        self.assertIn('outside_skill', [error['error'] for error in result['errors']])

    def test_doctor_handles_non_git_directory_and_does_not_claim_browser(self):
        plain = Path(self.temp.name) / 'plain'
        plain.mkdir()
        result = self.cli('doctor', '--root', str(plain))
        self.assertFalse(result['git']['worktree'])
        self.assertEqual(result['capabilities']['browser'], 'external_cli_required')
        self.assertEqual(result['capabilities']['shell'], 'rcode_permission_required')

    def test_install_dry_run_never_changes_rcode_state(self):
        skills = Path(self.temp.name) / 'skills'
        skill = skills / 'review'
        skill.mkdir(parents=True)
        (skill / 'SKILL.md').write_text('---\nname: review\ndescription: Review changes.\n---\nRead code.\n')
        executable = Path(self.temp.name) / 'rcode fixture'
        executable.write_text('#!/bin/sh\nprintf bad > install-ran\n')
        executable.chmod(0o700)
        result = self.cli('install', '--rcode', str(executable), '--project', str(self.root), '--skills', str(skills))
        self.assertFalse(result['executed'])
        self.assertEqual(result['argv'], [str(executable), '-C', str(self.root.resolve()), 'skills', 'link', '--name', 'rstack', str(skills.resolve())])
        self.assertFalse((self.root / 'install-ran').exists())

    def test_install_through_real_rcode_registers_the_expected_namespaced_skill(self):
        binary = os.environ.get('RCODE_BIN')
        if not binary:
            self.skipTest('RCODE_BIN указывает на реальный собранный rcode для интеграционной проверки link')
        skills = Path(self.temp.name) / 'skills'
        skill = skills / 'review'
        skill.mkdir(parents=True)
        (skill / 'SKILL.md').write_text('---\nname: review\ndescription: Review changes.\n---\nRead code.\n')
        self.env['RCODE_HOME'] = str(Path(self.temp.name) / 'state')
        result = self.cli('install', '--rcode', binary, '--project', str(self.root),
                          '--skills', str(skills), '--execute')
        self.assertTrue(result['executed'])
        self.assertEqual(result['exit_code'], 0)
        listed = subprocess.run([binary, '-C', str(self.root), '--json', 'skills', 'list'],
                                env=self.env, capture_output=True, text=True, timeout=10, check=True)
        rows = [json.loads(line) for line in listed.stdout.splitlines()]
        self.assertTrue(any(row.get('id') == 'rstack:review' and row.get('status') == 'active' for row in rows))


if __name__ == '__main__':
    unittest.main()
