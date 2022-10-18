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
        
        
if __name__ == '__main__':
    unittest.main()
