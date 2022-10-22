import unittest
from word import Word
from language import Language
from anagram import Anagram

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

    def test_boil_down(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('fur')
        language.boil_down(word)

        self.assertEqual({'f','r','fr'}, language.onset)
        self.assertEqual({'u'}, language.nucleus)
        self.assertEqual({'f','r','rf'}, language.coda)


    def test_build_syllables(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('fur')
        anagram = Anagram(word, language)
        anagram.boil_down_language()
        syllables = sorted(['fur','ur','uf','fu','urf','fru','ruf','ru','u'])
        syll = sorted([i.word for i in list(language.build_syllables(word))])
        self.assertEqual(syllables, syll)
        self.assertEqual({'f','r','fr'}, anagram.language.onset)


if __name__ == '__main__':
    unittest.main()

