#!/usr/bin/python

from anagram import Anagram
from word import Word
from language import Language

import sys
import logging
import argparse


def main(argv):

    logging.basicConfig(format='%(asctime)s-%(levelname)s- %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50))

    parser.add_argument("-l", "--language", default="german.txt", metavar="<filename>", help="the file containing the language data")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
    parser.add_argument("word", help="the word to be anagrammatized")
    args = parser.parse_args()

    logger.info("args: %s", args)
    logger.info('word is "%s"',args.word)
    logger.info('language is "%s"',args.language)

    anagram = Anagram(Word(args.word), Language(args.language))
    anagram.prepare()
    anagrams = anagram.anagram()
    logger.info('%d anagrams have been found', len(anagrams))
    logger.info('results: "%s"',anagrams)

if __name__ == "__main__":
    main(sys.argv[1:])

