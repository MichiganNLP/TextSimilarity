#!/usr/bin/env python2

import os, sys, imp
sys.path.append(os.path.abspath('../lib'))
from word2veccompare import initialize_vocabulary, compare
config_path = os.path.abspath('./config')
config = imp.load_source('config', config_path, open(config_path, 'r'))
from bs4 import BeautifulSoup

# TODO: read semafor output xml

# initialize_vocabulary(config.WORD2VEC_MODEL)
