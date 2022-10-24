import unittest
from anagram import Anagram
from word import Word
from language import Language
from copy import deepcopy
class TestAnagram(unittest.TestCase):

    def test_inventory(self):
        anagram = Anagram(Word('bcbcba'), Language('smurf.txt'))
        self.assertEqual(anagram.inventory,['a','b','c'])

    def test_count(self):
        anagram = Anagram(Word('bcbcba'), Language('smurf.txt'))
        self.assertEqual(anagram.count, [1,3,2])

    def test_subtract(self):
        anagram = Anagram(Word('bcbcba'), Language('smurf.txt'))
        word2 = Word('bcbxy')
        (difference, spare) = anagram.subtract(word2)
        self.assertEqual(difference, [1,1,1])
        self.assertEqual(spare, ['x','y'])

    def test_language(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(Word('bcbcba'), language)
        self.assertEqual(anagram.language.nucleus, {'u'})


    def test_set_slist(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('furu')
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        s_list = anagram.set_slist()
        self.assertEqual(['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'u', 'uf', 'ur', 'urf'], s_list)

    def test_set_i2syll(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('furu')
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        s_list = anagram.set_slist()
        i2syll = anagram.set_i2syll(s_list)
        self.assertEqual(i2syll,{0:'fru',1:'fu',2:'fur',3:'ru',4:'ruf',5:'u',6:'u',7:'uf',8:'ur',9:'urf'})

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

    def test_add_kvsum(self):
        tupdict = {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2}}
        tupdict = Anagram.add_kvsum(tupdict,(2,),(4,), Word('xyyyyzzz'))
        self.assertEqual(tupdict, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2},(2,4):{'x':1,'y':4,'z':3}})

        del tupdict[(2,4)]

        # don't add if key already exists
        tupdict[(2,4)] = {}
        tupdict = Anagram.add_kvsum(tupdict,(2,),(4,), Word('xyyyyzzz'))
        self.assertEqual(tupdict, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2},(2,4):{}})

        del tupdict[(2,4)]

        # don't add if word hasn't got enough letters
        tupdict = Anagram.add_kvsum(tupdict,(2,),(4,), Word('xyyyzzz'))
        self.assertEqual(tupdict, {(2,):{'x':1,'y':2,'z':3},(4,):{'y':2}})

    def test_cat(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('fur')
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        slist = anagram.set_slist()
        print("slist = ", slist)
        i2syll = anagram.set_i2syll(slist)
        syll2letters = anagram.set_syll2letters()
        print("syll2letters = ", syll2letters)
        combinations = dict([((i,),syll2letters[anagram.slist[i]]) for i in range(len(anagram.slist))])
        print("combinations= ", combinations)
        anagram.combinations = combinations
        anagram.cat((1,),2,3)
        print("combinations= ", combinations)
        # nothing should have been added because there can't be more than one
        # syllable (as there is only one nucleus/vowel)
        self.assertEqual((8,), max(combinations.keys()))

        

if __name__ == '__main__':
    unittest.main()
