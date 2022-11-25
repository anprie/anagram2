import unittest
from anagram import Anagram
from word import Word
from language import Language
from copy import deepcopy
import logging

logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.WARN)


class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.smurf = Language('smurf.txt')
        self.smurf.read()
        self.german = Language('german.txt')
        self.german.read()
        self.word = Word('furu')
        self.wordx = Word('xyyyzzz')
        self.wordy = Word('xyyyyzzz')

    def test_language(self):
        anagram = Anagram(Word('bcbcba'), self.smurf)
        self.assertEqual(anagram.language.nucleus, {'u'})

    def test_set_slist(self):
        anagram = Anagram(self.word, self.smurf)
        anagram.language.boil_down(self.word)
        anagram.language.build_syllables(self.word)
        s_list = anagram.set_slist()
        self.assertEqual(['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf'], s_list)

    def test_set_i2syll(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(self.word, language)
        anagram.language.boil_down(self.word)
        anagram.language.build_syllables(self.word)
        s_list = anagram.set_slist()
        i2syll = anagram.set_i2syll()
        self.assertEqual(i2syll,{0:'fru',1:'fu',2:'fur',3:'ru',4:'ruf',5:'u',6:'uf',7:'ur',8:'urf'})

    def test_set_syll2letters(self):
        anagram = Anagram(self.word, self.smurf)
        anagram.language.boil_down(self.word)
        anagram.language.build_syllables(self.word)
        syll2letters = anagram.set_syll2letters()
        syllables = ['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf']
        s2l = {'fru':{'f':1,'r':1,'u':1}, 'fu':{'f':1,'u':1},
        'fur':{'f':1,'r':1,'u':1}, 'ru':{'r':1,'u':1},
        'ruf':{'f':1,'r':1,'u':1}, 'u':{'u':1}, 'uf':{'f':1,'u':1},
        'ur':{'r':1,'u':1}, 'urf':{'f':1,'r':1,'u':1}}
        self.assertEqual(syll2letters,s2l)

    def test_set_syllcnt(self):
        anagram = Anagram(self.word, self.smurf)
        anagram.language.read(self.word)
        anagram.language.build_syllables(self.word)
        syllcnt = {0:1, 1:1, 2:1, 3:1, 4:1, 5:2, 6:1, 7:1, 8:1}
        anagram.set_slist()
        anagram.set_syllcnt()
        self.assertEqual(syllcnt, anagram.syllcnt)
        self.assertEqual(['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf'], anagram.slist)

    def test_add_kvsum(self):
        anagram = Anagram(self.wordy, self.german)
        anagram.combinations = {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2}}
        anagram.add_kvsum((2,),(4,))
        self.assertEqual(anagram.combinations, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2},(2,4):{'x':1,'y':4,'z':3}})

        del anagram.combinations[(2,4)]

        # don't add if key already exists
        anagram.combinations[(2,4)] = {}
        anagram.add_kvsum((2,),(4,))
        self.assertEqual(anagram.combinations, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2},(2,4):{}})

        del anagram.combinations[(2,4)]

        # don't add if word hasn't got enough letters
        anagram2 = Anagram(self.wordx,self.german)
        anagram2.prepare()
        anagram2.add_kvsum((2,),(4,))
        self.assertEqual(anagram.combinations, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2}})

    def test_cat(self):
        anagram = Anagram(self.word,self.smurf)
        anagram.prepare()
        # anagram.slist = ['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf']
        # anagram.i2syll = {0:'fru',1:'fu',2:'fur',3:'ru',4:'ruf',5:'u',6:'uf',7:'ur',8:'urf'}
        for i in range(len(anagram.slist)):
            anagram.cat((i,),i)
        # nothing should have been added because there can't be more than one syllable (as there is only one nucleus/vowel)
        self.assertEqual((8,), max(anagram.combinations.keys()))

        anagram2 = Anagram(self.word,self.smurf)
        anagram2.prepare()
        # anagram2.syllcnt = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1}
        keys = [(0,),(0,5),(1,),(1,3),(1,5),(1,7),(2,),(2,5),(3,),(3,5),(3,6),(4,),(4,5),(5,),(5,5),(5,6),(5,7),(5,8),(6,),(6,7),(7,),(8,)]
        for i in range(len(anagram2.slist)):
            anagram2.cat((i,),i)
        self.assertEqual(sorted(keys), sorted(anagram2.combinations.keys()))

    def test_anagram(self):
        anagram = Anagram(self.word, self.smurf)
        anagram.prepare()
        anagrams = anagram.anagram()
        expected = {'fru-u','fu-ru','fur-u','fu-ur','ru-uf','ruf-u','u-urf','uf-ur'}
        self.assertEqual(expected, anagrams)
        stringsums = [len(string) for string in list(anagrams)]
        self.assertTrue(all(s== len(anagram.word.word)+1 for s in stringsums))

    def test_prepare(self):
        anagram = Anagram(Word('tuna'), self.smurf)
        anagram.prepare()
        self.assertEqual({'u'}, anagram.language.nucleus)
        self.assertEqual(set(), anagram.language.onset)
        self.assertEqual(set(), anagram.language.coda)
        self.assertEqual(1, len(anagram.language.syllables))

        anagram2 = Anagram(Word('hello'), self.smurf)
        anagram2.prepare()
        self.assertEqual(set(), anagram2.language.nucleus)
        self.assertEqual(set(), anagram2.language.onset)
        self.assertEqual(set(), anagram2.language.coda)
        self.assertEqual(set(), anagram2.language.syllables)

        anagram3 = Anagram(Word('ru'), self.smurf)
        anagram3.prepare()
        self.assertEqual({'u'}, anagram3.language.nucleus)
        self.assertEqual({'r'}, anagram3.language.onset)
        self.assertEqual({'r'}, anagram3.language.coda)
        self.assertEqual(3, len(anagram3.language.syllables))

    def test_process(self):
        results  = Anagram.process('ru', 'smurf.txt')
        self.assertEqual({'ur','ru'}, results)

        results2 = Anagram.process('ru', 'german')
        self.assertEqual({'ur','ru'}, results2)

if __name__ == '__main__':
    unittest.main()
