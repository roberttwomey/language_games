from nltk import wordnet
import WNutils
import random
import os
from nltk.tokenize import regexp_tokenize
import warnings
import sys
import string
from time import localtime, strftime

def next_output_file(outpath):
    i=1;
    (base, extension)=os.path.splitext(outpath)
    timestamp=strftime("%Y%m%d", localtime())
    outfile=os.path.join(base+'_'+timestamp+'_'+str(i)+'.txt')    
    while os.path.exists(outfile):
        i+=1
        outfile=os.path.join(base+'_'+timestamp+'_'+str(i)+'.txt')
    return outfile

def main():
    # check arguments and usage
    if len(sys.argv)==3:
        in_file=sys.argv[1]
        out_file=sys.argv[2]
    else:
        print('usage: python mutate_file.py /path/to/input /path/to/output')
        print('will add a date and increment a file number to the end of the output filename')
        sys.exit()


    warnings.simplefilter("ignore")        

    print("opening "+in_file)
    in_f=open(in_file, encoding = "ISO-8859-1")

    next_out_file=next_output_file(out_file)

    print("writing to "+ next_out_file)

    out_f=open(next_out_file, "w")

    # look for properly formatted header on input file:
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
        print("read entire file without finding appropriately formed header.  exiting.")
        out_f.close()
        exit

    # start
    print("parsing contents:",)

    # read the file a line at a time, and transform
    for line in in_f:
            mut_line=WNutils.mutateLine(line)
            out_f.write(mut_line);
            out_f.write('\n')

    print("done.")
    in_f.close()
    out_f.close()


if __name__ == '__main__':
        main()
