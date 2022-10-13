import re
import copy
from word import Word

class Anagram:

    def __init__(self, word, language):
        self.word = word
        self.inventory = sorted(word.letters.keys())
        self.count = [word.letters[key] for key in sorted(word.letters.keys())]
        self.language = copy.deepcopy(language)

    def __str__(self):
        return f"word: {self.word.word}\ninventory: {self.inventory}\noccurrences of letters in inventory: {self.count}"

    def subtract(self,word):
        result = copy.deepcopy(self.count)
        not_in_inventory = []
        for key in word.letters.keys():
            contains_letter = False
            for i in range(len(self.inventory)):
                if key == self.inventory[i]:
                    result[i]-= word.letters[key]
                    contains_letter = True
                    break
            if not contains_letter:
                not_in_inventory.append(key)
        return (result, not_in_inventory)

    def boil_down_language(self):
        for c_set in [self.language.onset, self.language.nucleus, self.language.coda]:
            for cluster in list(c_set):
                c = Word(cluster)
                if not self.word.contains(c):
                    c_set.remove(cluster)
        #print("remaining clusters:\n", self.language.onset, "\n",self.language.nucleus, "\n", self.language.coda, "\n")
        return


