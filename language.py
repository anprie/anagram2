import re
import copy

class Language:

    def __init__(self, lang_file):
        self.file = lang_file
        self.name = lang_file.split(sep='.', maxsplit=1)[0]
        self.onset = set()
        self.coda = set()
        self.nucleus = set()
        
    def __str__(self):
        return f"language: {self.name}\nfile: {self.file}\nonset: {self.onset}\nnucleus: {self.nucleus}\ncoda: {self.coda}"

    def read(self):
        # open file 
        #################################
        # lines look like this: cluster with distributional information
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
