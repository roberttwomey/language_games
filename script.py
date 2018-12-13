#!/usr/bin/python
#import nltk
import WNutils
import warnings
import sys
from operator import itemgetter

def main():
    warnings.simplefilter("ignore")
        
    if len(sys.argv)<2:
        in_file='/Users/rtwomey/script/script.txt'
        print "Parsing file "+in_file+"\n"
        WNutils.parse_file(in_file)
    else:
        for in_file in sys.argv[1:]:
            print "Parsing file "+in_file+"\n"
            WNutils.parse_file(in_file)
    
    print "\n"
    ##print "In WN:\n\n"+repr(WNutils.WNwords)
    sortedwords = sorted(WNutils.WNwords.iteritems(), key=itemgetter(1), reverse=True)
    for li in sortedwords:
        print li[0],
        print li[1]
    print "\n"

    print "\n"
##    print "Not in WN:\n\n"+repr(WNutils.nonWNwords)
    sortedwords = sorted(WNutils.nonWNwords.iteritems(), key=itemgetter(1), reverse=True)
    for li in sortedwords:
        print li[0],
        print li[1]
        
    print "\n"

    #for key,val in nonWNwords.iteritems():
    #        print key,val

    #for key,val in WNwords.iteritems():
    #        print key,val

    print "\n"
    print "words in WN: "+str(len(WNutils.WNwords))
    print "\n"
    print "words not in WN: "+str(len(WNutils.nonWNwords))

if __name__== '__main__':
        main()
