#!/usr/bin/python

# Short interactive shell program:
# to take input at command prompt
# and return a semantically altered version

import WNutils
import sys
import warnings
from IndexFile import IndexFile
from time import localtime, strftime
import os

characters = IndexFile()
props = IndexFile()
places = IndexFile()
materials = IndexFile()
memory = IndexFile()
photos = IndexFile()
things_shown = IndexFile()
script = IndexFile()

current=[]
out_f = ""
    
def load_references():
    print("loading characters...")
    characters.load_file("cast of characters - dramatis personae.txt")

    print("loading props...")
    props.load_file(r'props.txt')
    
    print("loading places...")
    places.load_file("places.txt")
    
    print("loading materials...")
    materials.load_file("physical material.txt")

    print("loading photos...")
    photos.load_file("photos in book.txt")

    print("loading things_shown...")
    things_shown.load_file("first year review - things Ive made.txt")

    print("loading database...")
    memory.load_file("computer folders.txt")

    print("loading script...")
    script.load_file("script.txt")
    
def check_input(line):
        global current
        if str(line).split()[0] == 'shift':
            for line in current:
                mut_line=WNutils.mutateLine(line, WNutils.broadest)
                print(mut_line)
                out_f.write('\n'+line+' ->\n')
                out_f.write(mut_line+'\n')    
        elif str(line).split()[0] == 'select' and len(str(line).split()) == 4:
            current=[]
            if str(line).split()[3]=='characters':
                i=int(str(line).split()[1])
                while i>0:        
                    term=characters.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            elif str(line).split()[3]=='props':
                i=int(str(line).split()[1])
                while i>0:        
                    term=props.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            elif str(line).split()[3]=='places':
                i=int(str(line).split()[1])
                while i>0:        
                    term=places.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            elif str(line).split()[3]=='materials':
                i=int(str(line).split()[1])
                while i>0:        
                    term=materials.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            elif str(line).split()[3]=='photos':
                i=int(str(line).split()[1])
                while i>0:        
                    term=photos.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            elif str(line).split()[3]=='things_shown':
                i=int(str(line).split()[1])
                while i>0:        
                    term=things_shown.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            elif str(line).split()[3]=='database':
                i=int(str(line).split()[1])
                while i>0:        
                    term=memory.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            elif str(line).split()[3]=='script':
                i=int(str(line).split()[1])
                while i>0:        
                    term=script.getranditem()
                    print(term)
                    out_f.write('\n'+term+'\n')
                    current.append(term)
                    i-=1
            else:
                mut_line=WNutils.mutateLine(line, WNutils.broadest)
                print(mut_line)
                current=mut_line
                out_f.write('\n'+line+' ->\n')
                out_f.write(mut_line+'\n')

        else:
            mut_line=WNutils.mutateLine(line, WNutils.broadest)
            print(mut_line)
            current=mut_line
            out_f.write('\n'+line+' ->\n')
            out_f.write(mut_line+'\n')
        out_f.flush()

def next_output_file(outpath):
    i=1;
    (base, extension)=os.path.splitext(outpath)
    timestamp=strftime("%Y%m%d", localtime())
    outfile=os.path.join(base+'_'+timestamp+'_'+str(i)+'.txt')    
    while os.path.exists(outfile):
        i+=1
        outfile=os.path.join(base+'_'+timestamp+'_'+str(i)+'.txt')
    return outfile

def cycle_next_output_file():
    global out_f
    out_f.close()
    # open new one
    new_fname=next_output_file("logs/log.txt")
    out_f=open(new_fname, "a")
    
def main():
    global out_f
    warnings.simplefilter("ignore")

    fname=next_output_file("logs/log.txt")
    out_f=open(fname, "a")
    os.system('clear')
    print("welcome to the interactive shell:")

    load_references()
    print(" ")
    line=""
    count=0
    while line != "quit" and line!=":q" and line!="exit":
        line=input(">")
        if len(line) > 0:
            check_input(line)
            print(" ")
            count+=1
            if count >= 100:
                cycle_next_output_file()
                count=0
    out_f.close()

if __name__ == '__main__':
    main()
    

