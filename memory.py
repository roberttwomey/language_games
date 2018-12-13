#!/usr/bin/python

import WNutils
import warnings
from operator import itemgetter

def main():
    warnings.simplefilter("ignore")
        
    dbpath='/Volumes/Swimming Pool/Memory'
    #dbpath='/Volumes/Reservoir/Assets/'
    print "Parsing file path "+dbpath+"\n"
    WNutils.walk_db(dbpath)

    ##print "\n"
    ##print "In WN:\n\n"+repr(WNutils.WNwords)
    ##print "\n"

    sortedwords = sorted(WNutils.WNwords.iteritems(), key=itemgetter(1), reverse=True)
    print "\n"
    for li in sortedwords:
        print li[0],
        print li[1]
        
    print "\n"

##    print "\n"
##    print "Not in WN:\n\n"+repr(WNutils.nonWNwords)
##    print "\n"

    sortedwords = sorted(WNutils.nonWNwords.iteritems(), key=itemgetter(1), reverse=True)
    print "\n"
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

if __name__ == '__main__':
    main()
