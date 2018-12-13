#!/usr/bin/python

import WNutils

WNutils.parse_file('/Users/rtwomey/script/people in photos.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/everyone in my reading reference.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/cast of characters - dramatis personae.txt')                                                          

print "\n"
print "In WN:\n\n"+repr(WNutils.WNwords)
print "\n"

print "\n"
print "Not in WN:\n\n"+repr(WNutils.nonWNwords)
print "\n"

#for key,val in nonWNwords.iteritems():
#        print key,val

#for key,val in WNwords.iteritems():
#        print key,val

print "\n"
print "words in WN: "+str(len(WNutils.WNwords))
print "\n"
print "words not in WN: "+str(len(WNutils.nonWNwords))
