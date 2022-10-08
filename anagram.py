import re
import copy

class Anagram:

    def __init__(self, word, language_file):
        self.word = word
        self.inventory = sorted(word.letters.keys())
        self.count = [word.letters[key] for key in sorted(word.letters.keys())]

    def __str__(self):
        return f"word: {self.word.word}\ninventory: {self.inventory}\noccurrences of letters in inventory: {self.count}"

    def subtract(self,word):
        result = copy.deepcopy(self.count)
        not_in_inventory = []
        for l in word.word:
            contains_letter = False
            for i in range(len(self.inventory)):
                if l == self.inventory[i]:
                    result[i]-=1
                    contains_letter = True
                    break
            if not contains_letter:
                not_in_inventory.append(l)
        return (result, not_in_inventory)



