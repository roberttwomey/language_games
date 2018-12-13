#
# 
#

import WNutils

#parse_file('/Users/rtwomey/script/script.txt')                                                          
#dbpath='/Volumes/Swimming Pool'
#walk_db(dbpath)
WNutils.parse_file('/Users/rtwomey/script/physical material.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/slightly more than shit.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/props.txt')                                                          
WNutils.parse_file('/Users/rtwomey/script/unassigned materials.txt')                                                          
#parse_file('/Users/rtwomey/script/visual memory reference.txt')                                                         
#parse_file('/Users/rtwomey/script/reference manuals reference.txt')                                                          


print "\n"
print "In WN:\n\n"+repr(WNutils.WNwords)
print "\n"

print "\n"
print "Not in WN:\n\n"+repr(WNutils.nonWNwords)
print "\n"

#for key,val in WNutils.nonWNwords.iteritems():
#        print key,val

#for key,val in WNutils.WNwords.iteritems():
#        print key,val

print "\n"
print "words in WN: "+str(len(WNutils.WNwords))
print "\n"
print "words not in WN: "+str(len(WNutils.nonWNwords))
