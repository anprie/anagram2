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


    # remove all syllables that can't be comprised of the input word's letters
    def boil_down_language(self):
        for c_set in [self.language.onset, self.language.nucleus, self.language.coda]:
            for c in list(c_set):
                if not self.word.contains(Word(c)):
                    c_set.remove(c)
        return (self.language.onset, self.language.nucleus, self.language.coda)


    # put onset, nucleus, and coda together to form syllables
    # add empty string to onset for syllables that start with a vowel
    def build_syllables(self):
        on = {Word(o+n) for o in self.language.onset.union({''}) for n in self.language.nucleus}
        onc = {Word(s+c) for c in self.language.coda for s in {i.word for i in on} if self.word.contains(Word(s+c))}
        self.syllables.update(on,onc)
        return self.syllables


    # return sorted list where each syllable appears as many times as it fits into the anagram.word.word
    def slist(self):
        s_list = []
        s_dict = dict([(w.word,w) for w in self.syllables])
        # self.sdict = s_dict?
        for s in list(self.syllables):
            cnt = self.word.contains(s)
            for i in range(cnt):
                s_list.append(s.word)
        return sorted(s_list)


    # map index to syllable string
    def i2syll(self,slist):
        index2syll = {}
        for i in range(len(slist)):
            index2syll[i] = slist[i]
        return index2syll

    # map syllable strings to syllable objects
    def syll2letters(self):
        syll2letters = dict([(s.word,s.letters) for s in self.syllables])
        return syll2letters

    # add new entry to dictionary: key = itup,jtup), value= sum of itup's and jtup's entries in tupdict
    # TODO: new parameter: letter dictionary of the input word. If v1+v2 is not contained in the input word, don't add the entry!
    def add_kvsum(tupdict, itup, jtup):
        tupdict[itup + jtup] = Word.add(tupdict[itup],tupdict[jtup])
        return tupdict

    def combine_syllables(self):
        # create dictionary with indices of slist as keys and the corresponding syllable's letter dict as values
        # loop through indices, adding entries to the dictionary
        pass

