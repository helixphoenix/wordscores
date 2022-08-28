from click.testing import CliRunner
from unittest import TestCase, mock
import pytest


@pytest.fixture()
def mock_cli():
    return CliRunner()


class TestMain(TestCase):
    mock_cli = CliRunner()

    @mock.patch("wordscores.wording.__main__.topwords")
    def test_topwords(self, mock_topwords):
        res = self.mock_cli.invoke(
            mock_topwords, ["--filepath", "/Users/duduok/Desktop/GitHub/wordscores/wording/wordlist.txt"]
        )
        assert res.exit_code == 0

    @mock.patch("wordscores.wording.__main__.letters")
    def test_topwords_from_letters(self, mock_letters):
        res = self.mock_cli.invoke(
            mock_letters,
            [
                "--letters",
                "deora",
            ],
        )
        assert res.exit_code == 0
