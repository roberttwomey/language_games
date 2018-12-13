#!/usr/bin/env python

"""
An echo server that uses threads to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select
import socket
import sys
import threading
import time, os
import glob
import random
import WNutils
import warnings
from IndexFile import IndexFile
from time import localtime, strftime

class Server:
    def __init__(self):
        
        self.log_file_list=[]
        self.playback_file=None
        self.filenum = 0

        self.characters = IndexFile()
        self.props = IndexFile()
        self.places = IndexFile()
        self.materials = IndexFile()
        self.memory = IndexFile()
        self.photos = IndexFile()
        self.things_shown = IndexFile()
        self.script = IndexFile()

        self.current=[]
        self.out_f = None
        

    def newest_file(self):
        root = './logs/' # one specific folder

        date_file_list = []
        for folder in glob.glob(root):
            #print "folder =", folder
            # select the type of file, for instance *.jpg or all files *.*
            for file in glob.glob(folder + '/*.*'):
                # retrieves the stats for the current file as a tuple
                # (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
                # the tuple element mtime at index 8 is the last-modified-date
                stats = os.stat(file)
                # create tuple (year yyyy, month(1-12), day(1-31), hour(0-23), minute(0-59), second(0-59),
                # weekday(0-6, 0 is monday), Julian day(1-366), daylight flag(-1,0 or 1)) from seconds since epoch
                # note:  this tuple can be sorted properly by date and time
                lastmod_date = time.localtime(stats[8])
                #print image_file, lastmod_date   # test
                # create list of tuples ready for sorting by date
                date_file_tuple = lastmod_date, file
                date_file_list.append(date_file_tuple)
         
        #print date_file_list  # test
         
        date_file_list.sort()
        date_file_list.reverse()  # newest mod date now first
         
        return date_file_list[0][1]

    def make_logfile_lists(self):        
        # root = '/home/robert/code/wordnet/nltk/logs/' # one specific folder
        root = './logs/' # one specific folder
        log_file_list = []
        for folder in glob.glob(root):
            for file in glob.glob(folder + '/*.txt'):
                self.log_file_list.append(file)

    def open_playback_file(self, filename):
        self.playback_file = open(filename,"r")

    def cycle_next_playback_file(self):
        self.playback_file.close()

        self.filenum+=1
        if self.filenum > len(self.log_file_list):
            self.filenum=0
        self.open_playback_file(self.log_file_list[self.filenum])

    def print_next_idle_line(self):
        line=""
        while line != '\n':
            line=self.playback_file.readline()
            if line=="":
                self.cycle_next_playback_file()
                print(" ")
            else:
                print(line,)
            sys.stdout.flush()

    def load_references(self):
        print("loading characters...")
        self.characters.load_file("cast of characters - dramatis personae.txt")
        
        print("loading props...")
        self.props.load_file("props.txt")
        
        print("loading places...")
        self.places.load_file("places.txt")
        
        print("loading materials...")
        self.materials.load_file("physical material.txt")

        print("loading photos...")
        self.photos.load_file("photos in book.txt")

        print("loading things_shown...")
        self.things_shown.load_file("first year review - things Ive made.txt")

        print("loading database...")
        self.memory.load_file("computer folders.txt")

        print("loading script...")
        self.script.load_file("script.txt")
        
    def check_input(self,line):
##            if str(line).split()[0] == 'shift':
##                #for line in self.current:
##                mut_line=WNutils.mutateLine(line, WNutils.broadest)
##                print self.current+'->\n'+mut_line
##                self.out_f.write('\n'+line+' ->\n')
##                self.out_f.write(mut_line+'\n')    
##            elif str(line).split()[0] == 'select' and len(str(line).split()) == 4:
##                self.current=[]
##                if str(line).split()[3]=='characters':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.characters.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                elif str(line).split()[3]=='props':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.props.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                elif str(line).split()[3]=='places':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.places.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                elif str(line).split()[3]=='materials':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.materials.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                elif str(line).split()[3]=='photos':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.photos.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                elif str(line).split()[3]=='things_shown':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.things_shown.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                elif str(line).split()[3]=='database':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.memory.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                elif str(line).split()[3]=='script':
##                    i=int(str(line).split()[1])
##                    while i>0:        
##                        term=self.script.getranditem()
##                        print term
##                        self.out_f.write('\n'+term+'\n')
##                        self.current.append(term)
##                        i-=1
##                else:
##                    mut_line=WNutils.mutateLine(line, WNutils.sisters)
##                    print '-> '+mut_line
##                    self.current=mut_line
##                    self.out_f.write('\n'+line+' ->\n')
##                    self.out_f.write(mut_line+'\n')
##
##            else:
            mut_line=WNutils.mutateLine(line, WNutils.sisters)
            print('-> '+mut_line)
            self.current=mut_line
            self.out_f.write('\n'+line+' ->\n')
            self.out_f.write(mut_line+'\n')
            self.out_f.flush()

    def next_output_file(self,outpath):
        i=1;
        (base, extension)=os.path.splitext(outpath)
        timestamp=strftime("%Y%m%d", localtime())
        outfile=os.path.join(base+'_'+timestamp+'_'+str(i)+'.txt')    
        while os.path.exists(outfile):
            i+=1
            outfile=os.path.join(base+'_'+timestamp+'_'+str(i)+'.txt')
        return outfile

    def cycle_next_output_file():
        self.out_f.close()
        # open new one
        new_fname=self.next_output_file("./logs/log.txt")
        #new_fname=self.next_output_file("/home/robert/code/wordnet/nltk/logs/log.txt")
        self.out_f=open(new_fname, "a")

    
    def run(self):
        self.make_logfile_lists()
        random.shuffle(self.log_file_list)
        #print repr(self.log_file_list)
        self.open_playback_file(self.log_file_list[0])
        
        filename = self.newest_file()
        
        idletime=0
        idlemode=False
        start_idling=20
        
        warnings.simplefilter("ignore")

        fname=self.next_output_file("./logs/log.txt")
        #fname=self.next_output_file("/home/robert/code/wordnet/nltk/logs/log.txt")
        self.out_f=open(fname, "a")
        os.system('clear')
        print("welcome to the interactive shell:")

        self.load_references()
        print(" ")
        
        running = True
        line=""
        count=0
        tick=0
        idlemode=False
        start_idling=60
        utterance_timing=1
        min_wait=15
        max_wait=30
        
        while running and line !="quit" and line!=":q" and line!="exit":
            input = [self.playback_file, sys.stdin]
            inputready,outputready,exceptready = select.select(input,[],[])
            if tick==0:
                sys.stdout.write(">")
                sys.stdout.flush()
            for s in inputready:
                if s == sys.stdin:
                    idlemode=False
                    tick=0
                    line = sys.stdin.readline().rstrip("\n")
                    self.check_input(line)
                    print(" ")
                    count+=1
                    if count >= 100:
                        self.cycle_next_output_file()
                        count=0
                elif s == self.playback_file:
                    #sys.stdout.write(".")
                    #sys.stdout.flush()
                    time.sleep(1)
                    tick+=1
                    
                    if tick>start_idling:
                        idlemode=True

                    if idlemode and tick>utterance_timing:
                        self.print_next_idle_line()
                        tick=0
                        utterance_timing=random.randint(min_wait, max_wait)
        self.out_f.close()

if __name__ == "__main__":
    random.seed()
    os.system('clear')
    
    s = Server()
    s.run() 
