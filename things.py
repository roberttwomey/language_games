#!/usr/bin/python

import WNutils

#dbpath='/Volumes/Swimming Pool'
#walk_db(dbpath)
WNutils.parse_file('/Users/rtwomey/script/physical material.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/slightly more than shit.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/props.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/unassigned materials.txt')                                                          

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
