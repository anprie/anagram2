import unittest
from word import Word
from language import Language

class TestLanguage(unittest.TestCase):

    def test_name(self):
        lang_file = "german.txt"
        language = Language(lang_file)
        self.assertEqual(language.name, "german")

    def test_read(self):
        language = Language("smurf.txt")
        language.read()
        self.assertEqual(language.onset, {'s','m','r','f','fr','sm'})
        self.assertEqual(language.nucleus, {'u'})
        self.assertEqual(language.coda, {'s','m','r','f','rm','rf','rs','sm','mf'})


if __name__ == '__main__':
    unittest.main()

