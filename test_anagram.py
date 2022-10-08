import unittest
from anagram import Anagram
from word import Word
class TestAnagram(unittest.TestCase):

    def test_inventory(self):
        word = Word('dcbaABCD')
        anagram = Anagram(word, 'german.txt')
        print(anagram)
        self.assertEqual(anagram.inventory,['a','b','c','d'])

    def test_count(self):
        word = Word('bcbcba')
        anagram = Anagram(word, 'german.txt')
        print(anagram)
        self.assertEqual(anagram.count, [1,3,2])

    def test_subtract(self):
        word = Word('bcbcba')
        anagram = Anagram(word, 'german.txt')
        word2 = Word('bcbxy')
        (difference, spare) = anagram.subtract(word2)
        self.assertEqual(difference, [1,1,1])
        self.assertEqual(spare, ['x','y'])


if __name__ == '__main__':
    unittest.main()
