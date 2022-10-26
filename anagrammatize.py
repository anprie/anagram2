#!/usr/bin/python

from anagram import Anagram
from word import Word
from language import Language

import sys, getopt
import logging

logging.basicConfig(format='%(asctime)s %(message)s')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)



def main(argv):
    word = ''
    language = ''
    try:
      opts, args = getopt.getopt(argv,"hw:l:",["word=","language="])
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
    print('word is "',word,'"')
    print('language is "',language,'"')
    anagram = Anagram(Word(word), Language(language))
    anagram.prepare()
    anagrams = anagram.anagram()
    print("results:")
    print(anagrams)

if __name__ == "__main__":
    main(sys.argv[1:])

