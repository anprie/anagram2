import unittest
from word import Word
from language import Language

class TestLanguage(unittest.TestCase):

    def test_name(self):
        lang_file = "german.txt"
        language = Language(lang_file)
        self.assertEqual(language.name, "german")

if __name__ == '__main__':
    unittest.main()

