#!/usr/bin/python

from anagram import Anagram
from word import Word
from language import Language

import sys, getopt
import logging

logging.basicConfig(format='%(asctime)s-%(levelname)s- %(message)s')

logger = logging.getLogger()

logger.setLevel(logging.INFO)



def main(argv):
    word = ''
    language = ''
    level = 'info'
    try:
      opts, args = getopt.getopt(argv,"hw:l:d:",["word=","language=", "debug="])
    except getopt.GetoptError:
      print( 'Usage:\n\tanagrammatize.py -w <word> -l <language_file>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('Usage:\n\tanagrammatize.py -w <word> -l <language_file>')
         sys.exit()
      elif opt in ("-w", "--word"):
         word = arg
      elif opt in ("-l", "--language"):
         language = arg
      elif opt in ("-d", "--debug"):
         level = arg
    logger.info('word is "%s"',word)
    logger.info('language is "%s"',language)
    anagram = Anagram(Word(word), Language(language))
    anagram.prepare()
    anagrams = anagram.anagram()
    logger.info('%d anagrams have been found', len(anagrams))
    logger.info('results: "%s"',anagrams)

if __name__ == "__main__":
    main(sys.argv[1:])

