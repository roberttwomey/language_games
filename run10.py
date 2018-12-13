#!/usr/bin/python
from WNutils import mutateWord
from WNutils import children
import sys
import warnings

warnings.simplefilter("ignore")

result=''

##out_f=open("logs/log.txt", "a")
##out_f.write("input: ")
##
##for arg in sys.argv[1:]:
##    out_f.write(arg+' ')

##out_f.write('\n')

i=0
while i < int(sys.argv[1]):
    result=''
    for arg in sys.argv[2:]:
        result+=mutateWord(arg, children).replace('_',' ')+' '
    i+=1
    print i,': ',
    print result
##    out_f.write(result+"\n")

##out_f.close()
