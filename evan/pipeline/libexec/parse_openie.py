#!/usr/bin/env python2

from sets import Set
from sys import argv
import os
import string

def output_sentence(index, sentence, alternatives, permuations_path):
    output_path = os.path.join(permuations_path, str(index) + '.txt')
    with open(output_path, 'w') as output_file:
        if len(alternatives) > 0:
            permuations = alternatives
        else:
            permuations = [sentence]
        for p in permuations:
            print >> output_file, p

def extract_sentences(file):
    sentences = {}
    for line in file:
        sentence, alternative = parse_line(line.rstrip())
        if sentence not in sentences:
            sentences[sentence] = Set([sentence])
        sentences[sentence].add(alternative)
    return sentences

def parse_line(line):
    split = line.split('\t')
    sentence = split[-1]
    alternative = parse_alternative(split[2:-1])
    return (sentence, alternative)

def parse_alternative(alternatives):
    result = []
    for alt in alternatives:
        formatted = alt.split('(', 1)[1].split(',', 1)[0]
        result.append(formatted)
    return string.join(result)

def main(output_path):

    openie_output_path = os.path.join(output_path, 'openie_output.txt')
    permuations_path = os.path.join(output_path, 'permutations')
    os.mkdir(permuations_path)

    with open(openie_output_path, 'r') as openie_output_file:
        sentences = extract_sentences(openie_output_file)

    for i, sentence in enumerate(sentences):
        permutations = sentences[sentence]
        perms_path = os.path.join(permuations_path, str(i + 1) + '.txt')
        with open(perms_path, 'w') as perm_file:
            for permutation in permutations:
                print>>perm_file, permutation

if __name__ == '__main__':
    output_path = argv[1]
    main(output_path)
