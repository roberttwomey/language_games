import sys

in_f = open("Assets_maplist.txt", "r")
for line in in_f:
    print str(line).split()[0]+', ',
    print str(line).split()[1]
    
