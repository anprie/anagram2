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

    def test_inventory(self):
        word = Word('dcbaABCD')
        inventory = word.inventory
        self.assertEqual(word.inventory,['a','b','c','d'])

    def test_count(self):
        word = Word('countletters')
        (count, spare) = word.count(word.word)
        self.assertEqual(count, [1,2,1,1,1,1,1,3,1])
        self.assertEqual(spare, [])

        word2 = Word('countxy')
        (count, spare) = word.count(word2.word)
        self.assertEqual(count, [1,0,0,1,1,0,0,1,1])
        self.assertEqual(spare, ['x','y'])

    def test_letters(self):
        word = Word('countletters')
        self.assertEqual(word.lcount, {'c':1,'e':2,'l':1,'n':1,'o':1,'r':1,'s':1,'t':3,'u':1})

    def test_difference(self):
        word = Word('abbccc')
        difference = word.difference(word)
        self.assertEqual(difference, [0,0,0])
        
        word2 = Word('abc')
        difference = word.difference(word2)
        self.assertEqual(difference, [0,1,2])

 

if __name__ == '__main__':
    unittest.main()
