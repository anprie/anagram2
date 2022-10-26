import re
import copy

class Word:

    def __init__(self, word):
        loweralpha = "".join([l.lower() for l in word if l.isalpha()])
        self.word = loweralpha
        self.letters = dict([(l,loweralpha.count(l)) for l in loweralpha])

    def __str__(self):
        return f"word: {self.word}\nhas letters: {self.letters}\n"


    def subtract(a,b):
        c = copy.deepcopy(a)
        for key in b.keys():
            c[key] = c.get(key,0) - b[key]
        return c

    def ldiff(self,word):
        return Word.subtract(self.letters, word.letters)

    def add(a,b):
        c = copy.deepcopy(a)
        for key in b.keys():
            c[key] = c.get(key,0) + b[key]
        return c

    def lsum(self,word):
        return Word.add(self.letters, word.letters)

    def contains(self,d):
        if type(d) == Word:
            d = d.letters
        diff = Word.subtract(self.letters,d)
        # more occurrences of at least one letter in word than in self.word
        if not all(v >= 0 for v in diff.values()):
            return 0
        # at least one letter has the same count in word and self.word; avoid dividing by 0
        if 0 in diff.values():
            return 1
        # how many times does word fit into self.word, letterwise?
        return min([self.letters[l]//d[l] for l in d])

