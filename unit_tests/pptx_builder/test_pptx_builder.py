from click.testing import CliRunner

from pptx_builder import cli


def test_pptx_builder_cli_with_one_yaml():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['unit_tests/pptx_builder/yamls/Amazing_grace.yml',
         '--pptx-template-path', 'unit_tests/pptx_builder/pptx-templates']
    )
    assert result.exit_code == 0


def test_pptx_builder_cli_with_many_yamls():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['unit_tests/pptx_builder/yamls/',
         '--pptx-template-path', 'unit_tests/pptx_builder/pptx-templates']
    )
    assert result.exit_code == 0
