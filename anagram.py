import re
import copy
from word import Word

class Anagram:

    def __init__(self, word, language):
        self.word = word
        self.inventory = sorted(word.letters.keys())# TODO: remove?
        self.count = [word.letters[key] for key in sorted(word.letters.keys())]
        self.language = copy.deepcopy(language)
        self.syll2letters = {}
        self.i2syll = {}
        self.slist = []
        self.combinations = {}

    def __str__(self):
        return f"word: {self.word.word}\ninventory: {self.inventory}\noccurrences of letters in inventory: {self.count}"


    # TODO: remove?
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


    # return sorted list where each syllable appears as many times as it fits into the anagram.word.word
    def set_slist(self):
        s_list = []
        s_dict = dict([(w.word,w) for w in self.language.syllables])
        # self.sdict = s_dict?
        for s in list(self.language.syllables):
            cnt = self.word.contains(s)
            for i in range(cnt):
                s_list.append(s.word)
        self.slist = sorted(s_list)
        return self.slist


    # map index to syllable string
    def set_i2syll(self,slist):
        index2syll = {}
        for i in range(len(slist)):
            index2syll[i] = slist[i]
        self.i2syll = index2syll
        return index2syll

    # map syllable strings to syllable objects
    def set_syll2letters(self):
        syll2letters = dict([(s.word,s.letters) for s in self.language.syllables])
        self.syll2letters = syll2letters
        return syll2letters

    # add new entry to self.combinatiosn: key = itup,jtup), value= sum of itup's and # jtup's entries in self.combinations
    # if v1+v2 is not contained in word, don't add the entry!
    # if itup or jtup are not in the self.combinations, don't add the entry
    def add_kvsum(self, itup, jtup, word):
        if itup + jtup in self.combinations.keys() or itup not in self.combinations.keys() or jtup not in self.combinations.keys():
            if itup + jtup in self.combinations.keys():
                print("key ", itup + jtup, " exists")
            if not itup in self.combinations.keys():
                print(itup, "not in dict")
            if not jtup in self.combinations.keys():
                print(jtup, " not in dict")
            return 0

        vsum = Word.add(self.combinations[itup],self.combinations[jtup])
        if word.contains(vsum):
            print("adding key ", itup + jtup, "with value ", vsum)
            self.combinations[itup + jtup] = vsum
        return self.combinations


    def cat(self,tup,i):
        if i >= len(self.slist) -1:
            return tup 

        self.add_kvsum(tup, (i,), self.word)

        if tup + (i,) in self.combinations.keys():
            print("new entry has been added, recursive calls for i = ", i)
            for k in range(i, len(self.slist)):
                return self.cat(tup+ (k,), k+1)

        return


        


