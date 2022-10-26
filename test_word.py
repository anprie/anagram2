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

        word = Word('')
        self.assertEqual(word.word, '')

        word = Word(':?&')
        self.assertEqual(word.word, '')

    def test_letters(self):
        word = Word('countletters')
        self.assertEqual(word.letters, {'c':1,'e':2,'l':1,'n':1,'o':1,'r':1,'s':1,'t':3,'u':1})

    def test_ldiff(self):
        word = Word('aaabbcd')
        word2 = Word('abc')

        diff = word.ldiff(word)
        self.assertEqual(diff, {'a':0, 'b':0, 'c':0, 'd':0})

        diff1 = word.ldiff(word2)
        self.assertEqual(diff1, {'a':2, 'b':1, 'c':0, 'd':1})

        diff2 = word2.ldiff(word)
        self.assertEqual(diff2, {'a':-2, 'b':-1, 'c':0, 'd':-1})

    def test_lsum(self):
        word = Word('aaabbcd')
        word2 = Word('abc')

        lsum = word.lsum(word2)
        self.assertEqual(lsum, {'a':4, 'b':3, 'c':2, 'd':1})

        lsum2 = word2.lsum(word)
        self.assertEqual(lsum2, {'a':4, 'b':3, 'c':2, 'd':1})

    def test_contains(self):
        word = Word('aaaabbbccd')
        word2 = Word('abc')

        w_in_w2 = word.contains(word2)
        self.assertEqual(w_in_w2, 2)

        w2_in_w = word2.contains(word)
        self.assertEqual(w2_in_w, 0)

        w_in_w = word.contains(word)
        self.assertEqual(w_in_w, 1)

if __name__ == '__main__':
    unittest.main()
