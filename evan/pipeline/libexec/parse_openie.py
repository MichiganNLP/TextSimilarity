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

def echo_sentence(sentence, alternatives):
    print 'SENTENCE: ' + sentence
    print 'ALTERNATIVES:',
    if len(alternatives) == 0:
        print 'none'
    else:
        for i, alternative in enumerate(alternatives):
            if i != 0:
                print '             ',
            print alternative
    print

def remove_openie_info(line):
    return line[7:]

def parse_alternatives(sentences, openie):
    sentence = None
    while sentence != '':
        sentence = sentences.readline().rstrip()
        if sentence == '':
            break
        alternatives = []
        openie_line = None
        openie.readline()
        while openie_line != '':
            openie_line = remove_openie_info(openie.readline().rstrip())
            if openie_line == '':
                break
            alternatives.append(openie_line)
        echo_sentence(sentence, alternatives)

def main(output_path):

    sentences_path = os.path.join(output_path, 'untabbed.txt')
    with open(sentences_path, 'r') as sentences_file:
        first_sentence = sentences_file.readline().rstrip()
        sentences_file.seek(0)
        openie_output_path = os.path.join(output_path, 'openie_output.txt')
        with open(openie_output_path, 'r') as openie_output_file:
            seek_to_relevant_output(first_sentence, openie_output_file)
            parse_alternatives(sentences_file, openie_output_file)

if __name__ == '__main__':
    output_path = argv[1]
    main(output_path)
