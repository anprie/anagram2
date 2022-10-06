import re

class Anagram:

    def __init__(self, word, language_file):
        self.word = word
        self.file = language_file
        self.language = language.split(sep='.', maxsplit=1)[0]

    def __str__(self):
        return f"word: {self.word}\nfile: {self.file}\nlanguage: {self.language}"

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


