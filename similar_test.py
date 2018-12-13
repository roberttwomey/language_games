from nltk import wordnet

##ret=[]
##for syns in wordnet.V['toss'].synsets():
##    print syns
##    for instance_of in syns.closure(wordnet.HYPERNYM, depth=1):
##        for result in instance_of.closure(wordnet.HYPONYM, depth=1):
##            ret.append(result)
##        for result in instance_of.closure(wordnet.INSTANCE_HYPONYM, depth=1):
##            ret.append(result)   
##    for instance_of in syns.closure(wordnet.INSTANCE_HYPERNYM, depth=1):
##        for result in instance_of.closure(wordnet.HYPONYM, depth=1):
##            ret.append(result)
##        for result in instance_of.closure(wordnet.INSTANCE_HYPONYM, depth=1):
##            ret.append(result)
##
##for a in ret:
##    print a

from nltk import wordnet
import WNutils
import random
import os
from nltk.tokenize import regexp_tokenize
import warnings

in_path='/Users/rtwomey/script/'
in_file='props.txt'
outpath='/Users/rtwomey/altscript/'

def next_output_file(filename):
    i=1;
    filebase=os.path.splitext(filename)[0]
    outfile=os.path.join(outpath, filebase+str(i)+'.txt')    
    while os.path.exists(outfile):
        i+=1
        outfile=os.path.join(outpath, filebase+str(i)+'.txt')
    return outfile

warnings.simplefilter("ignore")
    

in_fname=os.path.join(in_path, in_file)

print "opening "+in_fname

in_f=open(in_fname)

out_fname=next_output_file(in_file)

print "writing to "+ out_fname

out_f=open(out_fname, "w")

# look for properly formatted header:
# two empty lines, followed by text, followed by two more empty lines
double_newlines=0
lastline=''

for line in in_f:
        out_f.write(line)
        if line == '\n' and lastline=='\n':
            double_newlines=double_newlines+1
        lastline=line
        if double_newlines==2:
            #print "Found two double newlines"
            break

if double_newlines!=2:
    print "read entire file without finding appropriately formed header.  exiting."
    out_f.close()
    exit

print "parsing contents:",

# split the rest of the file into lines
pattern=r'''[A-Za-z]+|[0-9]+'''
for line in in_f:
        for token in regexp_tokenize(line, pattern):
            #print token,
            result = WNutils.mutateWord(token, WNutils.children)
            out_f.write(result.replace('_',' ')+' ',)
            #print result,
        out_f.write('\n')
        #print '\n'

print "done."
in_f.close()
out_f.close()
