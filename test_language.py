import unittest
from word import Word
from language import Language
from anagram import Anagram
import logging

logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s %(message)s')

logger = logging.getLogger()

logger.setLevel(logging.INFO)


class TestLanguage(unittest.TestCase):
    def setUp(self):
        self.german = Language("german.txt")
        self.smurf = Language("smurf.txt")
        self.word = Word('fur')

    def test_name(self):
        self.assertEqual(self.german.name, "german")

        language = Language('german.txt.txt')
        self.assertEqual(language.name, "german")

        language1 = Language('german')
        self.assertEqual(language1.name, "german")

    def test_read(self):
        self.smurf.read()
        self.assertEqual(self.smurf.onset, {'s','m','r','f','fr','sm'})
        self.assertEqual(self.smurf.nucleus, {'u'})
        self.assertEqual(self.smurf.coda, {'s','m','r','f','rm','rf','rs','sm','mf'})

        language = Language("smurf.txt")
        language.read(self.word)
        self.assertEqual(language.onset, {'r','f','fr'})
        self.assertEqual(language.nucleus, {'u'})
        self.assertEqual(language.coda, {'r','f','rf'})

    def test_boil_down(self):
        smurf = Language('smurf.txt')
        smurf.read()
        smurf.boil_down(self.word)

        self.assertEqual({'f','r','fr'}, smurf.onset)
        self.assertEqual({'u'}, smurf.nucleus)
        self.assertEqual({'f','r','rf'}, smurf.coda)

        german = Language('german.txt')
        german.read()
        german.boil_down(self.word)
        self.assertEqual({'f','r','fr'}, german.onset)
        self.assertEqual({'u'}, german.nucleus)
        self.assertEqual({'f','r','rf'}, german.coda)


    def test_build_syllables(self):
        smurf = Language('smurf.txt')
        smurf.read()
        syllables = sorted(['fur','ur','uf','fu','urf','fru','ruf','ru','u'])
        syll = sorted([i.word for i in list(smurf.build_syllables(self.word))])
        self.assertEqual(syllables, syll)

    def test_remove_vowel_clusters(self):
        somelanguage = Language('somelanguage.txt')
        somelanguage.nucleus = {'a','au','u','ou'}
        somelanguage.remove_vowel_clusters()
        self.assertEqual(somelanguage.nucleus, {'a','u','ou'})


if __name__ == '__main__':
    unittest.main()

