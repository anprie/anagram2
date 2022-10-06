import unittest
from anagram import Anagram

class TestAnagram(unittest.TestCase):

    def test_word(self):
        anagram = Anagram('remove \t\n\rw h i t e s p a c e', 'german.txt')
        word = anagram.word
        self.assertEqual(word, 'removewhitespace')

        anagram = Anagram('only,.%@-_?!´#+~*1^<>|letters', 'german.txt')
        word = anagram.word
        self.assertEqual(word, 'onlyletters')

        anagram = Anagram('LoWeRcAsE', 'german.txt')
        word = anagram.word
        self.assertEqual(word, 'lowercase')

    def test_inventory(self):
        anagram = Anagram('dcbaABCD', 'german.txt')
        inventory = anagram.inventory
        self.assertEqual(inventory,['a','b','c','d'])



if __name__ == '__main__':
    unittest.main()
