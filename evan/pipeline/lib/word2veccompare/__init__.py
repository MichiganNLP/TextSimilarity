#!/usr/bin/env python2

from math import sqrt
from sys import argv
import array


vocab = None


def read_int_from(file):
    result = ''
    c = ''
    while (c != ' ') and (c != '\n'):
        result += c
        c = file.read(1)
    return int(result)

def read_word_from(file):
    result = ''
    c = ''
    while c != ' ':
        result += c
        c = file.read(1)
    return result.lstrip()

def read_vector_from(file, size):
    return array.array('f', file.read(4 * size))

def normalize(v):
    total = 0
    for n in v:
        total += n * n
    total = sqrt(total)
    for i in xrange(len(v)):
        v[i] /= total
    return v

def parse_vocab_file(vocab_file):
    word_count = read_int_from(vocab_file)
    vector_size = read_int_from(vocab_file)
    vocab = {}
    for i in xrange(word_count):
        new_word = read_word_from(vocab_file)
        new_vector = read_vector_from(vocab_file, vector_size)
        vocab[new_word] = normalize(new_vector)
    return vocab

def cosine_distance(a, b):
    numerator = 0
    a_squared_sum = 0
    b_squared_sum = 0
    for i, a_i in enumerate(a):
        b_i = b[i]
        numerator += a_i * b_i
        a_squared_sum += a_i * a_i
        b_squared_sum += b_i * b_i
    denominator = sqrt(a_squared_sum) * sqrt(b_squared_sum)
    return float(numerator) / float(denominator)

def compare(word_a, word_b):
    global vocab
    if (word_a not in vocab) or (word_b not in vocab):
        return None
    a = vocab[word_a]
    b = vocab[word_b]
    return cosine_distance(a, b)

def initialize_vocabulary(vocab_path):
    global vocab
    with open(vocab_path, 'rb') as vocab_file:
        vocab = parse_vocab_file(vocab_file)
