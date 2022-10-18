import re
import copy

class Word:

    def __init__(self, word):
        loweralpha = "".join([l.lower() for l in word if l.isalpha()])
        self.word = loweralpha
        self.letters = dict([(l,loweralpha.count(l)) for l in loweralpha])

    def __str__(self):
        return f"word: {self.word}\nhas letters: {self.letters}\n"

    def ldiff(self,word):
        l1 = copy.deepcopy(self.letters)
        l2 = word.letters
        for key in l2.keys():
            if key in l1:
                l1[key] -= l2[key]
            else:
                l1[key] = -l2[key]
        return l1

    def lsum(self,word):
        l1 = copy.deepcopy(self.letters)
        l2 = word.letters
        for key in l2.keys():
            if key in l1:
                l1[key] += l2[key]
            else:
                l1[key] = l2[key]
        return l1

    def contains(self,word):
        diff = self.ldiff(word)
        # more occurrences of at least one letter in word than in self.word
        if not all(v >= 0 for v in diff.values()):
            return 0
        # at least one letter has the same count in word and self.word; avoid dividing by 0
        if 0 in diff.values():
            return 1
        # how many times does word fit into self.word, letterwise?
        return min([self.letters[l]//word.letters[l] for l in word.letters])

