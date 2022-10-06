import unittest
from anagram import Anagram

class TestAnagram(unittest.TestCase):

    def test_word(self):
        anagram = Anagram('remove \t\n\rw h i t e s p a c e', 'german.txt')
        print(anagram)
        word = anagram.word
        self.assertEqual(word, 'removewhitespace')

        anagram = Anagram('only,.%@-_?!´#+~*1^<>|letters', 'german.txt')
        print(anagram)
        word = anagram.word
        self.assertEqual(word, 'onlyletters')

        anagram = Anagram('LoWeRcAsE', 'german.txt')
        print(anagram)
        word = anagram.word
        self.assertEqual(word, 'lowercase')

        anagram = Anagram('Ümläuteß', 'german.txt')
        print(anagram)
        word = anagram.word
        self.assertEqual(word, 'ümläuteß')

    def test_inventory(self):
        anagram = Anagram('dcbaABCD', 'german.txt')
        print(anagram)
        inventory = anagram.inventory
        self.assertEqual(inventory,['a','b','c','d'])

    def test_count(self):
        word = 'countletters'
        anagram = Anagram(word, 'german.txt')
        print(anagram)
        count = anagram.count(word)
        self.assertEqual(count, [1,2,1,1,1,1,1,3,1])

    def test_letters(self):
        word = 'countletters'
        anagram = Anagram(word, 'german.txt')
        print(anagram)
        letters = anagram.letters(word)
        self.assertEqual(letters, {'c':1,'e':2,'l':1,'n':1,'o':1,'r':1,'s':1,'t':3,'u':1})
        



if __name__ == '__main__':
    unittest.main()
