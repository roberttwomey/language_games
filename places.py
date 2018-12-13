#!/usr/bin/python

from nltk import wordnet
from nltk.wordnet.stemmer import morphy

import WNutils

def is_hyponym_of(term1, term2):
    if term1 in wordnet.N:
        # find synset 1
        # find synset 2
        for synset in wordnet.N[term1][0].closure(wordnet.HYPERNYM):
            if term2 in synset:
                return True
        return False
    else:
        morphed_term=morphy(term1,'noun')
        if morphed_term!=None:
            if morphed_term in wordnet.N:
                for synset in wordnet.N[term1][0].closure(wordnet.HYPERNYM):
                    if term2 in synset:
                        return True
    return False

WNutils.parse_file('/Users/rtwomey/script/places.txt')                                                          

print "\n"
print "In WN:\n\n"+repr(WNutils.WNwords)
print "\n"

print "\n"
print "Not in WN:\n\n"+repr(WNutils.nonWNwords)
print "\n"

#for key,val in nonWNwords.iteritems():
#        print key,val

print "\n"
print "words in WN: "+str(len(WNutils.WNwords))
print "\n"
print "words not in WN: "+str(len(WNutils.nonWNwords))

##for key,val in WNutils.WNwords.iteritems():
##    if is_hyponym_of(key, 'location'):
##        print key+" is a location"

