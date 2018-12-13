#!/usr/bin/python
import nltk, sys

#if len(sys.argv) != 3:
#  sys.exit("usage: pathlength WORD1.POS.SENSENUM WORD2.POS.SENSENUM")

print 'loading wordnet'
wn = nltk.corpus.reader.wordnet.WordNetCorpusReader(nltk.data.find('corpora/wordnet'))
print 'done loading'
S = wn.synset
L = wn.lemma

print S('alligator.n.01').shortest_path_distance(S('cat.n.01'))
#print S(sys.argv[1]).shortest_path_distance(S(sys.argv[2]))
