import unittest
from word import Word
from language import Language
from anagram import Anagram

class TestLanguage(unittest.TestCase):

    def test_name(self):
        lang_file = "german.txt"
        language = Language(lang_file)
        self.assertEqual(language.name, "german")

        langfile2 = 'german.txt.txt'
        language2 = Language(langfile2)
        self.assertEqual(language2.name, "german")

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

        language2 = Language('german.txt')
        language2.read()
        language2.boil_down(word)
        self.assertEqual({'f','r','fr'}, language2.onset)
        self.assertEqual({'u'}, language2.nucleus)
        self.assertEqual({'f','r','rf'}, language2.coda)
        

    def test_build_syllables(self):
        language = Language('smurf.txt')
        language.read()
        word = Word('fur')
        language.boil_down(word)
        syllables = sorted(['fur','ur','uf','fu','urf','fru','ruf','ru','u'])
        syll = sorted([i.word for i in list(language.build_syllables(word))])
        self.assertEqual(syllables, syll)


if __name__ == '__main__':
    unittest.main()

