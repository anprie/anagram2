import re
import copy
from word import Word

class Anagram:

    def __init__(self, word, language):
        self.word = word
        self.language = copy.deepcopy(language)
        self.syll2letters = {}
        self.i2syll = {}
        self.slist = []
        self.combinations = {}

    def __str__(self):
        return f"Object Anagram\nword: {self.word.word}\nlanguage: {self.language.name}\nletters: {self.word.letters}"


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

    # add new entry to self.combinatiosn: key = tup,jtup), value= sum of tup's and # jtup's entries in self.combinations
    # if v1+v2 is not contained in word, don't add the entry!
    # if tup or jtup are not in the self.combinations, don't add the entry
    def add_kvsum(self, tup, jtup, word):
        if tup + jtup in self.combinations.keys() or tup not in self.combinations.keys() or jtup not in self.combinations.keys():
            if tup + jtup in self.combinations.keys():
                print("error: key ", tup + jtup, " exists already")
            if not tup in self.combinations.keys():
                print("error: ", tup, "not in dict")
            if not jtup in self.combinations.keys():
                print("error: ", jtup, " not in dict")
            return 0

        vsum = Word.add(self.combinations[tup],self.combinations[jtup])
        if word.contains(vsum):
            #print("adding key ", tup + jtup, "with value ", vsum)
            self.combinations[tup + jtup] = vsum
            return 1
        #print("not enough letters in word for ", vsum)
        return 0


    def cat(self,tup,i):
        #print("tup = ", tup, "i = ", i)
        if i >= len(self.slist):
            #print("terminating condition")
            return

        self.add_kvsum(tup, (i,), self.word)

# TODO: avoid recursive calls for duplicate syllables as syllables can appear multiple times in slist
#        duplicate = self.i2syll[tup[-1]] == self.i2syll[i]
#        if duplicate:
#            print("last syllable is same as current, skipping duplicates")
        for k in [tuple()] + [(j,) for j in range(i+1, len(self.slist))]:
            #print("k = ", k)
            for m in range(i+1, len(self.slist)):
                #print("m = ", m)
                if k == tuple():# and not duplicate:
                    #print("k is empty tuple and current syllable is not a duplicate")
                    return self.cat(tup+k, m)
                if m>k[0]:# and k != tuple()
                    #print("k is not empty tuple and m is > k")
                    return self.cat(tup+k, m)

    def anagram(self):
        for i in range(len(self.slist)):
            self.cat((i,),i+1)
        anagrams = [[self.i2syll[x] for x in tup] for tup in self.combinations.keys() if self.word.letters == self.combinations[tup]]
#        print("anagrams =\n", anagrams)
#        print("joined strings:\n", ["-".join(a) for a in anagrams])
        return set(["-".join(a) for a in anagrams])

    def prepare(self):
        self.language.read(self.word)
        self.language.build_syllables(self.word)
        if self.language.nucleus == set():
            print("word and language have no vowel in common!")
        if self.language.syllables == set():
            print("could not build syllables that can be comprised of letters in word!")

        self.set_slist
        self.set_i2syll
        self.set_syll2letters

        return self.slist
