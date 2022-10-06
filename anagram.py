import re

class Anagram:

    def __init__(self, word, language):
        loweralpha = [l.lower() for l in word if l.isalpha()]
        self.word = "".join(loweralpha)
        self.file = language
        self.language = language.split(sep='.', maxsplit=1)[0]
        self.inventory = sorted(list(set(loweralpha)))

    def __str__(self):
        return f"word: {self.word}\ninventory: {self.inventory}\nlanguage: {self.language}"

    def letters(self, word):
        letters = {}
        L = list(word)
        for l in L:
            if l in letters:
                letters[l] +=1
            else:
                letters[l] = 1
        return letters

    def count(self, word):
        inventory = self.inventory
        count = [0 for l in inventory]
        for l in word:
            for i in range(len(self.inventory)):
                if l == self.inventory[i]:
                    count[i]+=1
                    break
        print("count = ", count)
        return count
        



