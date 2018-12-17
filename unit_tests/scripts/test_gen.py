from click.testing import CliRunner

from scripts import gen


def test_gen_with_one_yaml():
    runner = CliRunner()
    result = runner.invoke(
        gen.cli,
        ['unit_tests/scripts/yamls/Amazing_grace.yml',
         '--pptx-template-path', 'unit_tests/scripts/pptx-templates']
    )
    assert result.exit_code == 0


def test_gen_with_wildcard():
    runner = CliRunner()
    result = runner.invoke(
        gen.cli,
        ['unit_tests/scripts/yamls/',
         '--pptx-template-path', 'unit_tests/scripts/pptx-templates']
    )
    assert result.exit_code == 0
