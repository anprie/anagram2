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

    def test_boil_down_language(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(Word('smurf'), language)
        (onset, nucleus, coda) = (language.onset, language.nucleus, language.coda)
        anagram.boil_down_language()
        self.assertEqual(onset, anagram.language.onset)
        self.assertEqual(nucleus, anagram.language.nucleus)
        self.assertEqual(coda, anagram.language.coda)

        anagram2 = Anagram(Word('fur'), language)
        (onset, nucleus, coda) = (deepcopy(language.onset), deepcopy(language.nucleus), deepcopy(language.coda))
        anagram2.boil_down_language()
        self.assertEqual({'f','r','fr'}, anagram2.language.onset)
        self.assertEqual({'u'}, anagram2.language.nucleus)
        self.assertEqual({'f','r','rf'}, anagram2.language.coda)

        # language object unchanged
        self.assertEqual(onset, language.onset)
        self.assertEqual(nucleus, language.nucleus)
        self.assertEqual(coda, language.coda)

    def test_build_syllables(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(Word('fur'), language)
        anagram.boil_down_language()
        syllables = sorted(['fur','ur','uf','fu','urf','fru','ruf','ru','u'])
        syll = sorted([i.word for i in list(anagram.build_syllables())])
        self.assertEqual(syllables, syll)
        self.assertEqual({'f','r','fr'}, anagram.language.onset)


    def test_slist(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(Word('furu'), language)
        anagram.boil_down_language()
        anagram.build_syllables()
        s_list = anagram.slist()
        self.assertEqual(['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'u', 'uf', 'ur', 'urf'], s_list)

    def test_i2syll(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(Word('furu'), language)
        anagram.boil_down_language()
        anagram.build_syllables()
        s_list = anagram.slist()
        i2syll = anagram.i2syll(s_list)
        self.assertEqual(i2syll,{0:'fru',1:'fu',2:'fur',3:'ru',4:'ruf',5:'u',6:'u',7:'uf',8:'ur',9:'urf'})

    def test_syll2letters(self):
        language = Language('smurf.txt')
        language.read()
        anagram = Anagram(Word('fur'), language)
        anagram.boil_down_language()
        anagram.build_syllables()
        syll2letters = anagram.syll2letters()
        syllables = ['fru', 'fu', 'fur', 'ru', 'ruf', 'u', 'uf', 'ur', 'urf']
        s2l = {'fru':{'f':1,'r':1,'u':1}, 'fu':{'f':1,'u':1},
        'fur':{'f':1,'r':1,'u':1}, 'ru':{'r':1,'u':1},
        'ruf':{'f':1,'r':1,'u':1}, 'u':{'u':1}, 'uf':{'f':1,'u':1},
        'ur':{'r':1,'u':1}, 'urf':{'f':1,'r':1,'u':1}}
        self.assertEqual(syll2letters,s2l)


 
if __name__ == '__main__':
    unittest.main()
