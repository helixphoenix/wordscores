__author__ = "helixphoenix"

from ast import Or
import re

from collections import OrderedDict


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []
    starting_letters = ""

    def __init__(self, validwords, lettervalues):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        print(lettervalues)
        print(validwords)

        if lettervalues == "" or lettervalues == "":
            lettervalues = "/Users/duduok/Desktop/GitHub/wordscores/wording/letterValues.txt"
            with open(lettervalues) as f:
                for line in f:
                    (key, val) = line.split(":")
                    self.letter_values[str(key).strip().lower()] = int(val)

        elif type(lettervalues) == dict:
            self.letter_values = lettervalues

        else:

            with open(lettervalues) as f:
                for line in f:
                    (key, val) = line.split(":")
                    self.letter_values[str(key).strip().lower()] = int(val)

        if validwords == "":
            validwords = "/Users/duduok/Desktop/GitHub/wordscores/wording/wordlist.txt"
            with open(validwords) as f:
                self.valid_words = f.read().splitlines()

        elif type(validwords) == list:
            self.valid_words = validwords
        else:
            with open(validwords) as f:
                self.valid_words = f.read().splitlines()

    def validate_words(self):
        real_valid_words = []
        for word in self.valid_words:
            if len(word) > 3:
                real_valid_words.append(word)
        return real_valid_words

    def initial_words(self, words):
        word_count_dic = {}
        mini = 5
        maxi = 0
        for i in range(101):
            counter = 0
            for letter in list(words[i]):
                counter += self.letter_values[letter]
            if maxi < counter:
                maxi = counter
            if mini > counter:
                mini = counter
            word_count_dic[words[i]] = counter
            words.remove(words[i])
        word_count_dic = {k: v for k, v in sorted(word_count_dic.items(), key=lambda item: item[1])}
        return word_count_dic, words

    def leader_counter(self, word_count_dic, words, mini, maxi):
        for word in words:
            counter = 0
            for letter in list(word):
                counter += self.letter_values[letter]
            if maxi < counter:
                maxi = counter
            if mini < counter:
                word_count_dic[word] = counter
                if len(words) > 100:
                    rem = min(list(word_count_dic.items()))
                    word_count_dic.pop(rem[0])
        word_count_dic = {k: v for k, v in sorted(word_count_dic.items(), key=lambda item: item[1], reverse=True)}
        return word_count_dic

    def pretty_printer(self, tops):
        print("")
        print(f"===================================  HIGH SCORTED WORDS  =====================================")
        print("")
        for i in range(1, len(tops)):
            print(f"{i}. {list(tops.keys())[i]} with value : {list(tops.values())[i]}")
        print("")
        print("==============================================================================================")
        return print("")

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        #"""
        words = self.validate_words()
        if len(words) > 100:
            word_count_dic, words = self.initial_words(words)
            mini = min(word_count_dic.values())
            maxi = max(word_count_dic.values())
        else:
            word_count_dic = {}
            mini = 5
            maxi = 0
        top_words = self.leader_counter(word_count_dic, words, mini, maxi)
        return self.pretty_printer(top_words), "ok"

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.

        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """
        print(starting_letters)
        real_valid = self.validate_words()
        valid = ",".join(real_valid)
        bulls_count = {"bull": 0}
        for word in real_valid:
            if word == "bull":
                bulls_count[word] += 1
        pattern = ""
        for letter in list(starting_letters):
            pattern = pattern + "(\w*" + letter + ")"
        made_up_words = set(["".join(x) for x in re.findall(pattern, valid, flags=0)])
        mini = 5
        maxi = 0
        word_count_dic = {}
        top_words = self.leader_counter(word_count_dic, made_up_words, mini, maxi)
        print("How", top_words)
        return self.pretty_printer(top_words), "ok"
