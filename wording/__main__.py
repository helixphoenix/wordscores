import click
from wording.highscoringwords import HighScoringWords


@click.group()
def wordscores():
    pass


@wordscores.command()
@click.option(
    "--filepath",
    prompt="Please enter the file path for the words you want to top to",
    default="",
    prompt_required=False,
)
def topwords(filepath):
    TopWords = HighScoringWords(validwords=filepath, lettervalues="")
    TopWords.build_leaderboard_for_word_list()


@wordscores.command()
@click.option(
    "--letters",
    prompt="Please enter the letters you wished for the creation of the words you want to top to",
    required=True,
    type=str,
)
def letters(letters):
    TopWords = HighScoringWords(validwords="", lettervalues="")
    TopWords.build_leaderboard_for_letters(letters)


if __name__ == "__main__":
    wordscores()
