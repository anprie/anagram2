import re
import copy

class Anagram:

    def __init__(self, word, language_file):
        self.word = word
        self.file = language_file
        self.language = language_file.split(sep='.', maxsplit=1)[0]
        self.inventory = sorted(word.letters.keys())
        self.count = [word.letters[key] for key in sorted(word.letters.keys())]

    def __str__(self):
        return f"word: {self.word.word}\nfile: {self.file}\nlanguage: {self.language}"

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

    def read(self):
        # declare three empty sets (onset, nucleus, coda)
        # open file with clusters
        #################################
        # lines look like this:
        # mfp 0 0 1
        # äu 1 1 1
        # st 1 0 1
        # str 1 0 0
        #################################
        # parse lines: 
        #   split into cluster, o, n, c
        #   create Word object of cluster
        #   test if cluster letters are subset of word letters
        #   if yes:
        #       1 1 1 -> nucleus
        #       1 0 0 -> onset
        #       0 0 1 -> coda
        #       1 0 1 -> coda and onset
        pass


