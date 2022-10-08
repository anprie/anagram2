import re
import copy

class Word:

    def __init__(self, word):
        self.passed = word
        loweralpha = "".join([l.lower() for l in word if l.isalpha()])
        self.word = loweralpha
        self.letters = dict([(l,loweralpha.count(l)) for l in loweralpha])

    def __str__(self):
        return f"word: {self.word}\nhas letters: {self.inventory}\n"

    # counts how many times each of self's unique letters occurs in word 
    # if the input word contains letters that are not in the inventory, return False
    # else return a list of numbers that represent the occurrences of self's letters in word, in the order of inventory

    def difference(self,word):
        l1 = copy.deepcopy(self.letters)
        l2 = word.letters
        for key in l2.keys():
            if key in l1:
                l1[key] -= l2[key]
            else:
                l1[key] = -l2[key]
        return l1




