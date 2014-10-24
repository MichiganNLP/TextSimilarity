#!/usr/bin/env python2

from sys import argv
import os

def seek_to_relevant_output(sentence, file):
    looking_for = '[info] ' + sentence
    line = ''
    while line != looking_for:
        line = file.readline().rstrip()
        if line == looking_for:
            file.seek(-len(looking_for) - 1, os.SEEK_CUR)

def main(output_path):

    sentences_path = os.path.join(output_path, 'untabbed.txt')
    with open(sentences_path, 'r') as sentences_file:
        first_sentence = sentences_file.readline().rstrip()

    openie_output_path = os.path.join(output_path, 'openie_output.txt')
    with open(openie_output_path, 'r') as openie_output_file:
        seek_to_relevant_output(first_sentence, openie_output_file)
        print openie_output_file.read()

if __name__ == '__main__':
    output_path = argv[1]
    main(output_path)
