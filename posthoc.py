import os
import sys

base="computer folders"
ext="_20090211_2"
filename1="/Users/rtwomey/script/"+base+".txt"
filename2="/Users/rtwomey/altscript/"+base+ext+".txt"
#filename1=sys.argv[1]
#filename2=sys.argv[2]

outfilename="logs/posthoc_"+base+ext+".txt"

in_f1=open(filename1,"r")
in_f2=open(filename2,"r")

out_f=open(outfilename,"w")

for line in in_f1:
    line2=in_f2.readline()
    line1alt=line.replace('\n',' ')
    out_f.write(line1alt+"->\n")
    out_f.write(line2+"\n")

