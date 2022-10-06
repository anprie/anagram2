import unittest
from anagram import Anagram

class TestAnagram(unittest.TestCase):

    def test_word(self):
        anagram = Anagram('remove w h i t e s p a c e', 'german.txt')
        word = anagram.word
        self.assertEqual(word, 'removewhitespace')



if __name__ == '__main__':
    unittest.main()
