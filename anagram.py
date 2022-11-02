import re
import copy
from word import Word
from language import Language
import logging

logger = logging.getLogger()

class Anagram:

    def __init__(self, word, language):
        self.word = word
        self.language = copy.deepcopy(language)
        self.syll2letters = {}
        self.i2syll = {}
        self.slist = []
        self.syllcnt = {}
        self.combinations = {}
        self.max_sylls = 0

    def __str__(self):
        return f"Object Anagram\nword: {self.word.word}\nlanguage: {self.language.name}\nletters: {self.word.letters}"


    # return sorted list where each syllable appears as many times as it fits into the anagram.word.word
    def set_slist(self):
        self.slist = sorted([w.word for w in self.language.syllables])
        logger.debug("slist: %s", self.slist)
        return self.slist


    # map index to syllable string
    def set_i2syll(self):
        self.i2syll = dict([(i, self.slist[i]) for i in range(len(self.slist))])
        logger.debug("i2syll: %s", self.i2syll)
        return self.i2syll

    # map syllable strings to syllable objects
    def set_syll2letters(self):
        syll2letters = dict([(s.word,s.letters) for s in self.language.syllables])
        self.syll2letters = syll2letters
        logger.debug("syll2letters: %s", self.syll2letters)
        return syll2letters

    # how many times does each syllable fit into self.word.word?
    # dict syllable string: count
    def set_syllcnt(self):
        self.syllcnt = dict([(i, self.word.contains(Word(self.slist[i]))) for i in range(len(self.slist))])
        logger.debug("syllcnt: %s", str(self.syllcnt))
        self.max_sylls = sum([self.syllcnt[i] for i in range(len(self.slist))])
        logger.debug("max_sylls: %s", self.max_sylls)
        return self.syllcnt

    # add new entry to self.combinatiosn: key = (tup,jtup), value= sum of tup's and # jtup's entries in self.combinations
    # if v1+v2 is not contained in word, don't add the entry!
    # if tup or jtup are not in the self.combinations, don't add the entry
    def add_kvsum(self, tup, jtup, word):
        if tup + jtup in self.combinations.keys() or tup not in self.combinations.keys() or jtup not in self.combinations.keys():
            if tup + jtup in self.combinations.keys():
                logger.warning("key %s exists already", tup + jtup)
            if not tup in self.combinations.keys():
                logger.warning("%s not in self.combinations", tup)
            if not jtup in self.combinations.keys():
                logger.warning("%s not in self.combinations", jtup)
            return 0

        vsum = Word.add(self.combinations[tup],self.combinations[jtup])
        if word.contains(vsum):
            logger.debug("adding key %s with value %s", tup + jtup, vsum)
            self.combinations[tup + jtup] = vsum
            return 1
        logger.debug("not enough letters in word for %s ", vsum)
        return 0


    # use self.slist, which is a list of unique syllables
    # append the same index to the tuple when adding another instance of the same syllable
    # one for loop for recursive call is enough
    def cat(self,tup,i):
        print("i = ", i)
        #if i >= len(self.slist) or len(tup) >= sum([self.syllcnt[i] for i in range(len(self.slist))]):
        if i >= len(self.slist) or len(tup) >= self.max_sylls:
            logger.debug("terminating condition: tup = %s, i = %s ", tup, i)
            return

        added = self.add_kvsum(tup, (i,), self.word)

        if not added:
            logger.debug("no entry with key %s + (%s,) added", tup, i)
            return

        # number of instances that fit into word minus instances already in tup 
        # current instance is not yet in tup, therefore 1, not 0
        repeat_i = int(self.syllcnt[i]- tup.count(i)  > 1)

        for j in range(i + 1 - repeat_i, len(self.slist)):
            return self.cat(tup + (i,), j)


    # start computation of anagrams, filter results (discard dead ends with to few letters)
    def anagram(self):
        for i in range(len(self.slist)):
            self.cat((i,), i+1)
        logger.debug("combinations: %s", self.combinations)
        anagrams = [[self.i2syll[x] for x in tup] for tup in self.combinations.keys() if self.word.letters == self.combinations[tup]]
        logger.debug("anagrams: %s", anagrams)
        return set(["-".join(a) for a in anagrams])


    # build attributes before calculating anagrams
    def prepare(self):
        self.language.read(self.word)
        self.language.build_syllables(self.word)
        if self.language.nucleus == set():
            logger.warning("word and language have no vowel in common!")
        if self.language.syllables == set():
            logger.warning("could not build syllables that can be comprised of letters in word!")

        slist = self.set_slist()
        self.set_i2syll()
        self.set_syll2letters()
        self.set_syllcnt()
        self.combinations = dict([((i,),self.syll2letters[self.slist[i]]) for i in range(len(self.slist))])
        logger.debug("combinations: %s", self.combinations)

        return self.combinations

    # wrapper for the whole process from object creation to output of results
    # the caller has to know nothing about the class
    def process(wstring, lfile):
        a = Anagram(Word(wstring), Language(lfile))
        a.prepare()
        return a.anagram()
