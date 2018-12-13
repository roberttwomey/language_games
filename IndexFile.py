# Script/character/material interface:
# to select items from my reference files

import os
import random
import string
db_path="/Users/rtwomey/script/"

class IndexFile:
    def load_file(self, f_name):
        self.file_name=f_name
        joined=os.path.join(db_path, self.file_name)
        in_f=open(joined, "r", encoding = "ISO-8859-1")
        # in_f=open(joined, "r")

        # look for properly formatted header on input file:
        # two empty lines, followed by text, followed by two more empty lines
        double_newlines=0
        lastline=''
        for line in in_f:
                if line == '\n' and lastline=='\n':
                    double_newlines=double_newlines+1
                lastline=line
                if double_newlines==2:
                    #print "Found two double newlines"
                    break
                
        line=""
        for line in in_f:
            if line!='\n':
                self.items.append(line.strip())
            #print line

        in_f.close()

    def getitem(self, i):
        return self.items[i]

    def getranditem(self):
        return self.items[random.randint(0, len(self.items)-1)]
    def __len__(self):
        return len(self.items)

    def __init__(self):
        self.items=[]
        self.desc=""
        random.seed()
        
  
    
def main():
    characters = IndexFile("places.txt")
    print("item 1: "+characters.getitem(1))
        
if __name__ == '__main__':
    main()
