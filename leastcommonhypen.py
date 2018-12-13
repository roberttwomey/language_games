#!/usr/bin/python

import nltk.corpus.reader.wordnet, sys

if len(sys.argv) != 3:
  sys.exit("usage: leastcommonhypen WORD1.POS.SENSENUM WORD2.POS.SENSENUM")

print 'loading wordnet'
wn = nltk.corpus.reader.wordnet.WordNetCorpusReader(nltk.data.find('corpora/wordnet'))
print 'done loading'
S = wn.synset
L = wn.lemma

#print S('alligator.n.01').shortest_path_distance(S('cat.n.01'))
print S(sys.argv[1]).lowest_common_hypernyms(S(sys.argv[2]))
