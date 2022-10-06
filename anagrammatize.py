#!/usr/bin/python

from anagram import Anagram

import sys, getopt

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
    anagram = Anagram(word, language)
    anagram.set_letters()
    print(anagram)

if __name__ == "__main__":
    main(sys.argv[1:])

