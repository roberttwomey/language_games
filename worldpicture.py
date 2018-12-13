#!/usr/local/bin/python

#import WNutils
import warnings
from operator import itemgetter
from nltk.tokenize import regexp_tokenize
import os
import sys
from WNutils import checkWN
from WNutils import relatedness, find_synsets, synsets_relatedness
import random

words={}

ignore_list=["DSC", "illus", "Store", "Clip", "MOV", "and", "Images", "stills", "the", ".DS_Store"]

class Sequencer:
    def __init__(self):
        self.terms=[]
        self.directory=''

    def build(self, directory):
        self.directory = directory

        for f in os.listdir(directory):
            if os.path.splitext(f)[1]=='.txt':
                self.terms.append(os.path.splitext(f)[0])
                #print f+',',


    def reorder(self):
        random.shuffle(self.terms)

        length = len(self.terms)-1

        print "========"
        print "unsorted list:", self.terms
        x=0
        max_score=0
        while (x<length):
            print "Passage n.: ",x+1
            print "(%.2f) %s ->" % (max_score, self.terms[x]),
            max_score=0
            y = x+1
            synsets1=find_synsets(self.terms[x])
            if synsets1!=[]:                
                while (y < length):
                    synsets2=find_synsets(self.terms[y])
                    if synsets2!=[]:
                        score=synsets_relatedness(synsets1, synsets2)
                        print "%0.3f"%score,
                        if score > max_score:
                            max_score=score
                            print '*',
                            self.terms[x+1], self.terms[y] = self.terms[y], self.terms[x+1]
                    else:
                        print '.',
                    y+=1
                    sys.stdout.flush()
            x+=1 
        print "========"
        print "sorted list:", self.terms

def ignore(token):
    if ignore_list.count(token) > 0:
        return True
    return False


def updatedictionary(token):
    if token not in words:
        words[token]=1
    else:
        words[token]=words[token]+1


def walk_db(rootpath):
        pattern=r'''[A-Za-z]+'''

        for root, dirs, files in os.walk(rootpath, followlinks=True):

                local_base=os.path.basename(os.path.relpath(root,rootpath))

                for base_token in regexp_tokenize(local_base, pattern):
                        if(len(base_token)>2) and ignore(base_token)==False:
                            #print base_token,
                            for f in files:
                                updatedictionary(base_token)
                            

                #print ":\n"
                for f in files: 
                        file_base=os.path.splitext(f)[0]
                        for token in regexp_tokenize(file_base, pattern):
                                if(len(token)>2) and ignore(token)==False:
                                        #print token,
                                        updatedictionary(token)

                if 'web' in dirs:
                    dirs.remove('web')
                if '.svn' in dirs:
                    dirs.remove('.svn')

            
def checktarget(token, target):
    if token==target:
        return True
    else:
        return False


def make_file_list(sortedwords, rootpath):
    pattern=r'''[A-Za-z]+'''

    for li in sortedwords:        
        target=li[0]
        count=0
        sys.stdout.write(target+" ")
        sys.stdout.flush()
        out_fname='./terms/'+target+'.txt'
        out_f=open(out_fname, "w")
        
        for root, dirs, files in os.walk(rootpath, followlinks=True):

                    local_base=os.path.basename(os.path.relpath(root,rootpath))
                        
                    for base_token in regexp_tokenize(local_base, pattern):
                        if(len(base_token)>2) and ignore(base_token)==False:
                            if base_token==target:
                                for f in files:
                                    #print os.path.join(root, f)
                                    out_f.write(os.path.join(root, f)+'\n')
                                    count+=1

                    for f in files: 
                            file_base=os.path.splitext(f)[0]
                            for token in regexp_tokenize(file_base, pattern):
                                    if(len(token)>2) and ignore(token)==False:
                                            if token==target:
                                                #print os.path.join(root, f)
                                                out_f.write(os.path.join(root, f)+'\n')
                                                count+=1

                    if 'web' in dirs:
                        dirs.remove('web')
        print li[1],
        print "expected,",
        print count,
        print "found."
                                                            

def main():
    warnings.simplefilter("ignore")

    timeline = Sequencer()
    timeline.build('./terms')
    timeline.reorder()
    
##    dbpath='/Volumes/Reservoir/Assets/'
    #dbpath='/Volumes/Swimming Pool/Memory/Pink Wig'
    #print "Parsing file path "+dbpath+"\n"
##    walk_db(dbpath)

##    sortedwords = sorted(words.iteritems(), key=itemgetter(1), reverse=True)
    #print "\n"
    #print "Words sorted by frequency:\n\n"+repr(sortedwords)
    #for li in sortedwords:
    #    print li[0],
    #    print li[1]

##    make_file_list(sortedwords, dbpath) 



if __name__ == '__main__':
    main()
