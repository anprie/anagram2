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
        return self.syllcnt

    # add new entry to self.combinations: key = tup+jtup, value= sum of tup's and jtup's entries 
    # if v1+v2 doesn't fit into self.word, don't add the entry
    # if tup or jtup are not in the self.combinations, don't add the entry
    def add_kvsum(self, tup, jtup):
        if tup + jtup in self.combinations.keys() or tup not in self.combinations.keys() or jtup not in self.combinations.keys():
            if tup + jtup in self.combinations.keys():
                logger.warning("key %s exists already", tup + jtup)
            if not tup in self.combinations.keys():
                logger.warning("%s not in self.combinations", tup)
            if not jtup in self.combinations.keys():
                logger.warning("%s not in self.combinations", jtup)
            return 0

        vsum = Word.add(self.combinations[tup],self.combinations[jtup])
        if self.word.contains(vsum):
            logger.debug("adding key %s with value %s", tup + jtup, vsum)
            self.combinations[tup + jtup] = vsum
            return 1
        logger.debug("not enough letters in word for %s ", vsum)
        return 0


    # try to add all remaining indices to current tuple
    # if successful, recursive call for the added tuple
    # recursive call for same index only if there are instances of that syllable left
    def cat(self,tup,i):

        if tup not in self.combinations or i >= len(self.slist):
            logger.warning("cat called with illegal parameters %s, %s", tup, i)
            return

        for k in range(i, len(self.slist)):
            added = self.add_kvsum(tup, (k,))
            if added:
                if k == i and self.syllcnt[i] - tup.count(i) <= 1:
                    next
                self.cat(tup + (k,), k)

        return


    # start computation of anagrams, filter results (discard dead ends with too few letters)
    def anagram(self):
        for i in range(len(self.slist)):
            self.cat((i,), i)
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

        self.set_slist()
        self.set_i2syll()
        self.set_syll2letters()
        self.set_syllcnt()
        # initiate dictionary which is used by add_kvsum
        self.combinations = dict([((i,),self.syll2letters[self.slist[i]]) for i in range(len(self.slist))])
        logger.debug("combinations: %s", self.combinations)

        return self.combinations

    # wrapper for the whole process from object creation to output of results
    # the caller needs to know nothing about the class
    def process(wstring, lfile):
        if not lfile.endswith('.txt'):
            lfile = lfile + '.txt'
        a = Anagram(Word(wstring), Language(lfile))
        a.prepare()
        return a.anagram()
