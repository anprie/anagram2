import re
import copy
from word import Word

class Anagram:

    def __init__(self, word, language):
        self.word = word
        self.inventory = sorted(word.letters.keys())
        self.count = [word.letters[key] for key in sorted(word.letters.keys())]
        self.language = copy.deepcopy(language)
        self.syllables = set()

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
        discarded = 0
        for c_set in [self.language.onset, self.language.nucleus, self.language.coda]:
            for c in list(c_set):
                if not self.word.contains(Word(c)):
                    c_set.remove(c)
                    discarded += 1
        #print(discarded, " clusters have been discarded\n")
        return (self.language.onset, self.language.nucleus, self.language.coda)

    def create_syllables(self):
        onset= list(self.language.onset)
        onset.append('')

        for o in onset:
            for n in list(self.language.nucleus):
                # no test if letters of o and n sum up well because they are disjoint
                self.syllables.add(Word(o+n))

        for s in list(self.syllables):
            for c in list(self.language.coda):
                sc = Word(s.word+c)
                if self.word.contains(sc):
                    self.syllables.add(sc)
        return self.syllables


