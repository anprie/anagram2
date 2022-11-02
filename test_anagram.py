import unittest
from anagram import Anagram
from word import Word
from language import Language
from copy import deepcopy
import logging

logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s %(message)s')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


class TestAnagram(unittest.TestCase):

    def test_language(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(Word('bcbcba'), language)
        #print(anagram)
        self.assertEqual(anagram.language.nucleus, {'u'})


    def test_set_slist(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('furu')
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        s_list = anagram.set_slist()
        self.assertEqual(['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf'], s_list)

    def test_set_i2syll(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('furu')
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        s_list = anagram.set_slist()
        i2syll = anagram.set_i2syll()
        self.assertEqual(i2syll,{0:'fru',1:'fu',2:'fur',3:'ru',4:'ruf',5:'u',6:'uf',7:'ur',8:'urf'})

    def test_set_syll2letters(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('fur')
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        syll2letters = anagram.set_syll2letters()
        syllables = ['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf']
        s2l = {'fru':{'f':1,'r':1,'u':1}, 'fu':{'f':1,'u':1},
        'fur':{'f':1,'r':1,'u':1}, 'ru':{'r':1,'u':1},
        'ruf':{'f':1,'r':1,'u':1}, 'u':{'u':1}, 'uf':{'f':1,'u':1},
        'ur':{'r':1,'u':1}, 'urf':{'f':1,'r':1,'u':1}}
        self.assertEqual(syll2letters,s2l)

    def test_set_syllcnt(self):
        language = Language('smurf.txt')
        word = Word('furu')
        anagram = Anagram(word, language)
        anagram.language.read(word)
        anagram.language.build_syllables(word)
        syllcnt = {0:1, 1:1, 2:1, 3:1, 4:1, 5:2, 6:1, 7:1, 8:1}
        anagram.set_slist()
        anagram.set_syllcnt()
        self.assertEqual(syllcnt, anagram.syllcnt)
        self.assertEqual(['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf'], anagram.slist)


    def test_add_kvsum(self):
        word = Word('xyyyyzzz')
        anagram = Anagram(word, Language('german.txt'))
        anagram.combinations = {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2}}
        anagram.add_kvsum((2,),(4,),word )
        self.assertEqual(anagram.combinations, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2},(2,4):{'x':1,'y':4,'z':3}})

        del anagram.combinations[(2,4)]

        # don't add if key already exists
        anagram.combinations[(2,4)] = {}
        anagram.add_kvsum((2,),(4,), Word('xyyyyzzz'))
        self.assertEqual(anagram.combinations, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2},(2,4):{}})

        del anagram.combinations[(2,4)]

        # don't add if word hasn't got enough letters
        anagram.add_kvsum((2,),(4,), Word('xyyyzzz'))
        self.assertEqual(anagram.combinations, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2}})

    def test_cat(self):
        anagram = Anagram(Word('fur'),Language('smurf.txt'))
        anagram.prepare()
        # ['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf']
        # {0:'fru',1:'fu',2:'fur',3:'ru',4:'ruf',5:'u',6:'uf',7:'ur',8:'urf'}
        for i in range(len(anagram.slist)):
            anagram.cat((i,),i+1)
        # nothing should have been added because there can't be more than one syllable (as there is only one nucleus/vowel)
        self.assertEqual((8,), max(anagram.combinations.keys()))

        anagram2 = Anagram(Word('furu'),Language('smurf.txt'))
        anagram2.prepare()
        keys = [(0,),(0,5),(1,),(1,3),(1,5),(1,7),(2,),(2,5),(3,),(3,5),(3,6),(4,),(4,5),(5,),(5,6),(5,7),(5,8),(6,),(6,7),(7,),(8,)]
        filtered_keys = [(0,5),(1,3),(1,5),(1,7),(2,5),(3,5),(3,6),(4,5),(5,6),(5,7),(5,8),(6,7)]
        for i in range(len(anagram.slist)):
            anagram2.cat((i,),i+1)
        self.assertEqual(sorted(keys), sorted(anagram2.combinations.keys()))

    def test_anagram(self):
        word = Word('furu')
        language = Language('smurf.txt')
        anagram = Anagram(word, language)
        anagram.prepare()
        anagrams = anagram.anagram()
        expected = {'fru-u','fu-ru','fur-u','fu-ur','ru-uf','ruf-u','u-urf','uf-ur'}
        self.assertEqual(expected, anagrams)
        stringsums = [len(string) for string in list(anagrams)]
        #self.assertTrue(all(s== len(anagram.word.word)+1 for s in stringsums))

    def test_prepare(self):
        anagram = Anagram(Word('tuna'), Language('smurf.txt'))
        anagram.prepare()
        self.assertEqual({'u'}, anagram.language.nucleus)
        self.assertEqual(set(), anagram.language.onset)
        self.assertEqual(set(), anagram.language.coda)
        self.assertEqual(1, len(anagram.language.syllables))

        anagram2 = Anagram(Word('hello'), Language('smurf.txt'))
        anagram2.prepare()
        self.assertEqual(set(), anagram2.language.nucleus)
        self.assertEqual(set(), anagram2.language.onset)
        self.assertEqual(set(), anagram2.language.coda)
        self.assertEqual(set(), anagram2.language.syllables)

        anagram3 = Anagram(Word('ru'), Language('smurf.txt'))
        anagram3.prepare()
        self.assertEqual({'u'}, anagram3.language.nucleus)
        self.assertEqual({'r'}, anagram3.language.onset)
        self.assertEqual({'r'}, anagram3.language.coda)
        self.assertEqual(3, len(anagram3.language.syllables))

    def test_process(self):
        results  = Anagram.process('ru', 'smurf.txt')
        self.assertEqual({'ur','ru'}, results)

if __name__ == '__main__':
    unittest.main()
