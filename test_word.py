import unittest
from word import Word

class TestWord(unittest.TestCase):

    def test_word(self):
        word = Word('remove \t\n\rw h i t e s p a c e')
        self.assertEqual(word.word, 'removewhitespace')

        word = Word('only,.%@-_?!´#+~*1^<>|letters')
        self.assertEqual(word.word, 'onlyletters')

        word = Word('LoWeRcAsE')
        self.assertEqual(word.word, 'lowercase')

        word = Word('Ümläuteß')
        self.assertEqual(word.word, 'ümläuteß')

    def test_letters(self):
        word = Word('countletters')
        self.assertEqual(word.letters, {'c':1,'e':2,'l':1,'n':1,'o':1,'r':1,'s':1,'t':3,'u':1})

    def test_difference(self):
        word = Word('aaabbcd')
        word2 = Word('abc')

        difference = word.difference(word)
        self.assertEqual(difference, {'a':0, 'b':0, 'c':0, 'd':0})

        difference1 = word.difference(word2)
        self.assertEqual(difference1, {'a':2, 'b':1, 'c':0, 'd':1})

        difference2 = word2.difference(word)
        self.assertEqual(difference2, {'a':-2, 'b':-1, 'c':0, 'd':-1})
 
    def test_lsum(self):
        word = Word('aaabbcd')
        word2 = Word('abc')
        
        lsum = word.lsum(word2)
        self.assertEqual(lsum, {'a':4, 'b':3, 'c':2, 'd':1})

if __name__ == '__main__':
    unittest.main()
