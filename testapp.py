#!/usr/bin/python
#import nltk, sys

#if len(sys.argv) != 3:
#  sys.exit("usage: pathlength WORD1.POS.SENSENUM WORD2.POS.SENSENUM")

#print 'loading wordnet.'
#wn = nltk.corpus.reader.wordnet.WordNetCorpusReader(nltk.data.find('corpora/wordnet'))
#S = wn.synset
#L = wn.lemma

import os
os.getcwd()      # gets current working directory - the equivalent of pwd
import glob
print glob.glob('*')     # lists all files in the current directory python is running in


#print S('alligator.n.01').shortest_path_distance(S('cat.n.01'))
#print S(sys.argv[1]).shortest_path_distance(S(sys.argv[2]))
