import re
import copy
from word import Word
import logging

logger = logging.getLogger()

class Language:

    def __init__(self, lang_file):
        self.file = lang_file
        self.name = lang_file.split(sep='.', maxsplit=1)[0]
        self.onset = set()      # of strings
        self.coda = set()       # of strings
        self.nucleus = set()    # of strings
        self.syllables = set()  # of Word objects

    def __str__(self):
        return f"language: {self.name}\nfile: {self.file}\nonset: {self.onset}\nnucleus: {self.nucleus}\ncoda: {self.coda}"

    def read(self, word = ''):
        if not word:
            logger.info("method read called without argument")
        with open(self.file) as file:
            lines = 0
            for line in file.readlines():
                lines += 1
                (cluster, o, n, c) = [a.strip() for a in line.split(' ')]
                if word and not word.contains(Word(cluster)):
                    continue
                if n == '1':
                    self.nucleus.add(cluster)
                    continue
                if o == '1':
                    self.onset.add(cluster)
                if c == '1':
                    self.coda.add(cluster)

        if self.nucleus == set():
            logger.warning("no vowels in language!")
        self.remove_vowel_clusters()
        return lines


    # remove all clusters that can't be comprised of the input word's letters
    def boil_down(self, word):
        for c_set in [self.onset, self.nucleus, self.coda]:
            for c in list(c_set):
                if not word.contains(Word(c)):
                    c_set.remove(c)
        if self.nucleus == set():
            logger.warning("no vowels in language!")
        return (self.onset, self.nucleus, self.coda)

    # remove complex clusters from nucleus if its letters are in nucleus
    # (those clusters will be built by concatenation)
    def remove_vowel_clusters(self):
        N = list(self.nucleus)
        for v in N:
            if  len(v)>1:
                if len({a for a in v if a in self.nucleus}) == len(v):
                    self.nucleus.remove(v)
        return self.nucleus


    # put onset, nucleus, and coda together to form syllables
    # add empty string to onset for syllables that start with a vowel
    def build_syllables(self, word):
        onset, nucleus, coda = self.boil_down(word)
        on = {Word(o+n) for o in onset.union({''}) for n in nucleus}
        onc = {Word(s+c) for c in coda for s in {i.word for i in on} if word.contains(Word(s+c))}
        self.syllables.update(on,onc)
        if self.syllables == {}:
            logger.warning("could not build syllables!")
        return self.syllables

