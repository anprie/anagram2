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
        return (self.language.onset, self.language.nucleus, self.language.coda)


    def build_syllables(self):
        on = {Word(o+n) for o in self.language.onset.union({''}) for n in self.language.nucleus}
        onc = {Word(s+c) for c in self.language.coda for s in {i.word for i in on} if self.word.contains(Word(s+c))}
        self.syllables.update(on,onc)
        return self.syllables


    def slist(self):
        # use contains to count how many instances of each syllable fit into
        # the input word
        s_list = []
        s_dict = dict([(w.word,w) for w in self.syllables])
        # self.sdict = s_dict?
        for s in list(self.syllables):
            cnt = self.word.contains(s)
            for i in range(cnt):
                s_list.append(s.word)
        return sorted(s_list)


    def i2syll(self,slist):
        # concatenate syllables, building a look-up table to calculate the remaining letters
        index2syll = {}
        for i in range(len(slist)):
            index2syll[i] = slist[i]
        # self.index2syll = index2syll?
        return index2syll

    def syll2letters(self):
        syll2letters = dict([(s.word,s.letters) for s in self.syllables])
        # self.syll2letters = syll2letters
        return syll2letters

    def add_comb(self,combinations, itup, j):
        # look up itups value in combinations (a dict)
        # look up j's value in combinations (a dict)
        # new entry in combinations is (itup,j) = sum of both values
        # we can't use lsum for this because it needs a word -> new function, make lsum use this
        # itup will be sorted so that we don't calculate each entry more than
        # once
        pass

