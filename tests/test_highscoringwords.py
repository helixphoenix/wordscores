#!/usr/bin/python3

from unittest import TestCase
from wording.highscoringwords import HighScoringWords


class TestHighScoringWords(TestCase):
    mock_letter_values = {"e": 1, "f": 4, "h": 4, "i": 1, "l": 1, "o": 1, "s": 1, "r": 1, "t": 1}
    very_valid_words = ["life", "is", "too", "short"]
    TestHighScoringWords = HighScoringWords(validwords=very_valid_words, lettervalues=mock_letter_values)

    def test_build_leaderboard_for_word_list(self):
        TestHighScoringWords = HighScoringWords(validwords=self.very_valid_words, lettervalues=self.mock_letter_values)
        res = TestHighScoringWords.build_leaderboard_for_word_list()
        assert res[1] == "ok"

    def test_build_leaderboard_for_letters(self):

        mock_starting_letters = "deora"
        TestHighScoringWords = HighScoringWords(validwords=self.very_valid_words, lettervalues=self.mock_letter_values)
        res = TestHighScoringWords.build_leaderboard_for_letters(mock_starting_letters)
        assert res[1] == "ok"
