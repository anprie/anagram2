import re

class Anagram:

    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.letters = None

    def __str__(self):
        return f"word: {self.word}\nletters: {self.letters}\nlanguage: {self.language}"

    def set_letters(self):
        letters = {}
        L = [l.lower() for l in self.word if l.isalpha()]
        for l in L:
            if l in letters:
                letters[l] +=1
            else:
                letters[l] = 1
        self.letters = letters




