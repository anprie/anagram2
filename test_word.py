import unittest
from word import Word

import logging
logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class TestWord(unittest.TestCase):
    def setUp(self):
        self.word1 = Word('aaabbcd')
        self.word2 = Word('abc')
        self.word3 = Word('aaaabbbccd')

    def test_word(self):
        word = Word('remove \t\n\rw h i t e s p a c e')
        self.assertEqual(word.word, 'removewhitespace')

        word = Word('only,.%@-_?!´#+~*1^<>|letters')
        self.assertEqual(word.word, 'onlyletters')

        word = Word('LoWeRcAsE')
        self.assertEqual(word.word, 'lowercase')

        word = Word('Ümläuteß')
        self.assertEqual(word.word, 'ümläuteß')

        word = Word('')
        self.assertEqual(word.word, '')

        word = Word(':?&')
        self.assertEqual(word.word, '')

    def test_letters(self):
        word = Word('countletters')
        self.assertEqual(word.letters, {'c':1,'e':2,'l':1,'n':1,'o':1,'r':1,'s':1,'t':3,'u':1})

    def test_ldiff(self):
        self.assertEqual(self.word1.ldiff(self.word1), {'a':0, 'b':0, 'c':0, 'd':0})
        self.assertEqual(self.word1.ldiff(self.word2), {'a':2, 'b':1, 'c':0, 'd':1})
        self.assertEqual(self.word2.ldiff(self.word1), {'a':-2, 'b':-1, 'c':0, 'd':-1})

    def test_lsum(self):
        self.assertEqual(self.word1.lsum(self.word2), {'a':4, 'b':3, 'c':2, 'd':1})
        self.assertEqual(self.word2.lsum(self.word1), {'a':4, 'b':3, 'c':2, 'd':1})

    def test_contains(self):
        self.assertEqual(self.word3.contains(self.word2), 2)
        self.assertEqual(self.word2.contains(self.word3), 0)
        self.assertEqual(self.word3.contains(self.word3), 1)

if __name__ == '__main__':
    unittest.main()
