import re
import copy
from word import Word

class Language:

    def __init__(self, lang_file):
        self.file = lang_file
        self.name = lang_file.split(sep='.', maxsplit=1)[0]
        self.onset = set()
        self.coda = set()
        self.nucleus = set()
        self.syllables = set()
        
    def __str__(self):
        return f"language: {self.name}\nfile: {self.file}\nonset: {self.onset}\nnucleus: {self.nucleus}\ncoda: {self.coda}"

    def read(self):
        with open(self.file) as file:
            lines = 0
            for line in file.readlines():
                lines += 1
                (cluster, o, n, c) = [a.strip() for a in line.split(' ')]
                if n == '1':
                    self.nucleus.add(cluster)
                    continue
                if o == '1':
                    self.onset.add(cluster)
                if c == '1':
                    self.coda.add(cluster)
        return lines


    # put onset, nucleus, and coda together to form syllables
    # add empty string to onset for syllables that start with a vowel
    def build_syllables(self, word):
        on = {Word(o+n) for o in self.onset.union({''}) for n in self.nucleus}
        onc = {Word(s+c) for c in self.coda for s in {i.word for i in on} if word.contains(Word(s+c))}
        self.syllables.update(on,onc)
        return self.syllables

