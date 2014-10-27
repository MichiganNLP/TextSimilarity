#!/usr/bin/env python2

from sys import argv
import os

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
        sentence, alternatives = parse_line(line.rstrip())
        if sentence not in sentences:
            sentences[sentence] = []
        sentences[sentence].append(alternatives)
    return sentences

def parse_line(line):
    split = line.split('\t')
    sentence = split[-1]
    alternatives = parse_alternatives(split[2:-1])
    return (sentence, alternatives)

def parse_alternatives(alternatives):
    result = []
    for alt in alternatives:
        formatted = alt.split('(', 1)[1].split(',', 1)[0]
        result.append(formatted)
    return result

def main(output_path):

    openie_output_path = os.path.join(output_path, 'openie_output.txt')
    permuations_path = os.path.join(output_path, 'permuations')
    os.mkdir(permuations_path)

    with open(openie_output_path, 'r') as openie_output_file:
        sentences = extract_sentences(openie_output_file)

    for sentence, alternatives in sentences.iteritems():
        print alternatives

if __name__ == '__main__':
    output_path = argv[1]
    main(output_path)
