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
        language = Language('smurf.txt')
        language.read()
        word = Word('fur')
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        slist = anagram.set_slist()
        i2syll = anagram.set_i2syll(slist)
        syll2letters = anagram.set_syll2letters()
        combinations = dict([((i,),syll2letters[anagram.slist[i]]) for i in range(len(anagram.slist))])
        anagram.combinations = combinations
        anagram.cat((1,),2)
        # nothing should have been added because there can't be more than one syllable (as there is only one nucleus/vowel)
        self.assertEqual((8,), max(combinations.keys()))

        word = Word('furu')
        anagram2 = Anagram(word, language)
        anagram2.language.boil_down(word)
        anagram2.language.build_syllables(word)
        slist = anagram2.set_slist()
        #['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'u', 'uf', 'ur', 'urf']
        #print("anagram.slist = ", anagram.slist)
        i2syll = anagram2.set_i2syll(slist)
        # i2syll =  {0: 'fru', 1: 'fu', 2: 'fur', 3: 'ru', 4: 'ruf', 5: 'u', 6: 'u', 7: 'uf', 8: 'ur', 9: 'urf'}
        #print("i2syll = ", i2syll)
        syll2letters = anagram2.set_syll2letters()
        combinations = dict([((i,),syll2letters[anagram2.slist[i]]) for i in range(len(anagram2.slist))])
        anagram2.combinations = combinations
        keys = [(0,),(0,5),(0,6),(1,),(1,3),(1,5),(1,6),(1,8),(2,),(2,5),(2,6),(3,),(3,5),(3,6),(3,7),(4,),(4,5),(4,6),(5,),(5,6),(5,7),(5,8),(5,9),(6,),(6,7),(6,8),(6,9),(7,),(7,8),(8,),(9,)]
        for i in range(len(anagram.slist)):
            anagram2.cat((i,),i+1)
        self.assertEqual(sorted(keys), sorted(anagram2.combinations.keys()))

    def test_anagram(self):
        word = Word('furu')
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(word, language)
        anagram.language.boil_down(word)
        anagram.language.build_syllables(word)
        slist = anagram.set_slist()
        i2syll = anagram.set_i2syll(slist)
        syll2letters = anagram.set_syll2letters()
        anagram.combinations = dict([((i,),syll2letters[anagram.slist[i]]) for i in range(len(anagram.slist))])
        # [(0,),(0,5),(0,6),(1,),(1,3),(1,5),(1,6),(1,8),(2,),(2,5),(2,6),(3,),(3,5),(3,6),(3,7),(4,),(4,5),(4,6),(5,),(5,6),(5,7),(5,8),(5,9),(6,),(6,7),(6,8),(6,9),(7,),(7,8),(8,),(9,)]
        # i2syll =  {0: 'fru', 1: 'fu', 2: 'fur', 3: 'ru', 4: 'ruf', 5: 'u', 6: 'u', 7: 'uf', 8: 'ur', 9: 'urf'}
        anagrams = anagram.anagram()
        filtered_combs = {('fru','u'),('fu','ru'),('fur','u'),('fu','ur'),('ru','uf'),('ruf','u'),('u','urf'),('uf','ur')}
        self.assertEqual(filtered_combs, anagrams)

        

if __name__ == '__main__':
    unittest.main()
