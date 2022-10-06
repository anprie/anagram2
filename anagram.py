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

    def letters(self):
        letters = {}
        L = list(self.word)
        for l in L:
            if l in letters:
                letters[l] +=1
            else:
                letters[l] = 1
        return letters

#    def inventory(self):
#        letter_set = set(list(self.word))
#        print("letter set: ",letter_set)
#        self.inventory = sorted(list(letter_set))
#        print("inventory: ", self.inventory)
#        return inventory

    def count(self):
        inventory = self.inventory
        count = [0 for l in inventory]
        for l in self.word:
            for i in range(len(self.inventory)):
                if l == self.inventory[i]:
                    count[i]+=1
                    break
        print("count = ", count)
        return count
        



