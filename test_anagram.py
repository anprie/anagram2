import unittest
from anagram import Anagram
from word import Word
class TestAnagram(unittest.TestCase):

    def test_inventory(self):
        anagram = Anagram(Word('bcbcba'), Language('smurf.txt'))
        self.assertEqual(anagram.inventory,['a','b','c','d'])

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
        anagram = Anagram(Word('bcbcba'), Language('smurf.txt'))
        self.assertEqual(self.language.nucleus, {'u'})

if __name__ == '__main__':
    unittest.main()
