#
# Interfaces to textual indices using Natural Language Toolkit
# WordNet Interface to evaluate and manipulate content.

# from nltk import wordnet

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
# from wordnet import morphy
# from nltk.corpus.wordnet import similarity
# from nltk.tokenize.regexp import WordTokenizer
from nltk.tokenize import regexp_tokenize
# from nltk.tokenize import RegexpTokenizer
import os
import random
import string

WNwords={}
nonWNwords={}

ignore_list=["the", "and", "you", "that", "with", "for", "this", "what", "something", "into", "they",
             "these", "from","how", "your", "which", "his", "when", "would", "could", "them", "where",
             "should", "she", "anything", "because", "our", "than", "everything", "their", "yourself",
             "her", "myself", "thats",
             "DSC", "illus", "Store", "Clip", "MOV", "and", "Images", "stills", "the", ".DS_Store"]

number_words=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
              "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
              "nineteen", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety",
              "hundred", "thousand", "million", "billion"]


hypo = lambda s: s.hyponyms()
hyper = lambda s:s.hypernyms()


def ignore(token):
        if ignore_list.count(token)>0:
                return True
        return False

def synonyms(synsets):
        return synsets
             
def sisters(synsets):
        ret=[]

        for synset in synsets:
            for instance_of in synset.closure(hypo, depth=1):
                for result in instance_of.closure(hypo, depth=1):
                    ret.append(result)
                # for result in instance_of.closure(wn.INSTANCE_HYPONYM, depth=1):
                #     ret.append(result)   
            for instance_of in synset.closure(hyper, depth=1):
                for result in instance_of.closure(hypo, depth=1):
                    ret.append(result)
            #     for result in instance_of.closure(wn.INSTANCE_HYPONYM, depth=1):
            #         ret.append(result)
        # print(synsets, ret)

        return ret

def children(synsets):
        ret=[]
        for synset in synsets:
                for child in synset.closure(hypo, depth=1):
                        ret.append(child)
        return ret

def broadest(synsets):
        ret=[]
        for synset in synsets:
            # sisters
            for instance_of in synset.closure(hyper, depth=1):
                for result in instance_of.closure(hypo, depth=1):
                    ret.append(result)
                # for result in instance_of.closure(wn.INSTANCE_HYPONYM, depth=1):
                #     ret.append(result)   
            # for instance_of in synset.closure(wn.INSTANCE_HYPERNYM, depth=1):
            #     for result in instance_of.closure(wn.HYPONYM, depth=1):
            #         ret.append(result)
            #     for result in instance_of.closure(wn.INSTANCE_HYPONYM, depth=1):
            #         ret.append(result)
            # children
            for child in synset.closure(hypo, depth=1):
                ret.append(child)
        return ret

def adverbs(synsets):
        # find synonyms and similar synsets
        ret=[]
        for synset in synsets:
                # for child in synset.closure(wn.hypernyms, depth=1):
                for child in synset.closure(hyper, depth=1):
                        ret.append(child)
        return synsets

def adjectives(synsets):
        # find synonyms and similar synsets
        ret=[]
        for synset in synsets:
                # for child in synset.closure(wn.SIMILAR, depth=1):
                for child in synset.similar_tos():#synset.hypernyms():
                        ret.append(child)
        return ret

def find_synsets(token):
        clean_token = token.lower()

        synsets=[]
        
        # try all parts of speech

        morphed_token=morphy(clean_token,'noun')
        if morphed_token != None:
                if morphed_token in wn.NOUN:
                        synsets+=wn.N[morphed_token].synsets()

        morphed_token=morphy(clean_token,'adj')
        if morphed_token != None:
                if morphed_token in wn.ADJ:
                        synsets+=wn.ADJ[morphed_token].synsets()

        morphed_token=morphy(clean_token,'verb')
        if morphed_token != None:
                if morphed_token in wn.VERB:
                        synsets+=wn.V[morphed_token].synsets()
        if clean_token in wn.ADV:
                synsets+=wn.ADV[clean_token].synsets()

        return synsets
        
def relatedness(token1, token2): #, sim_fn=similarity.path_similarity):
        # clean token1, token2
        clean_token1 = token1.lower()
        clean_token2 = token2.lower()

        synsets1=[]
        synsets2=[]

        # try all parts of speech
        if clean_token1 in wn.NOUN:
                synsets1+=wn.N[clean_token1].synsets()
        if clean_token1 in wn.ADJ:
                synsets1+=wn.ADJ[clean_token1].synsets()
        if clean_token1 in wn.VERB:
                synsets1+=wn.V[clean_token1].synsets()
        if clean_token1 in wn.ADV:
                synsets1+=wn.ADV[clean_token1].synsets()

        if clean_token2 in wn.NOUN:
                synsets2+=wn.N[clean_token2].synsets()
        if clean_token2 in wn.ADJ:
                synsets2+=wn.ADJ[clean_token2].synsets()
        if clean_token2 in wn.VERB:
                synsets2+=wn.V[clean_token2].synsets()
        if clean_token2 in wn.ADV:
                synsets2+=wn.ADV[clean_token2].synsets()

        #print synsets1
        #print synsets2

        max_score=0
        for syn1 in synsets1:
                for syn2 in synsets2:
                        # score=sim_fn(syn1, syn2)
                        syn1.path_similarlity(syn2)
                        if score>max_score:
                                max_score=score
        # try stemmed version
        # loop over all related synsets, all senses, find most related

        return max_score

# def synsets_relatedness(synsets1, synsets2, sim_fn=similarity.path_similarity, pos=['noun', 'verb', 'adjective', 'adverb']):
def synsets_relatedness(synsets1, synsets2, pos=['noun', 'verb', 'adjective', 'adverb']):
        max_score=0
        for syn1 in synsets1:
                if syn1.pos not in pos:
                        continue
                else:
                        for syn2 in synsets2:
                                if syn2.pos not in pos:
                                        continue
                                else:
                                        score=sim_fn(syn1, syn2)
                                        if score>max_score:
                                                max_score=score
        # try stemmed version
        # loop over all related synsets, all senses, find most related
        return max_score
        
def mutateWord(token, relfn=sisters):
        clean_token=token.lower()
        results=[]
        shifted_token=clean_token
        
        # try all parts of speech
        # if clean_token in wn.NOUN:
        #         results+=relfn(wn.NOUN[clean_token].synsets())
        # if clean_token in wn.ADJ:
        #         results+=adjectives(wn.ADJ[clean_token].synsets())
        # if clean_token in wn.VERB:
        #         results+=relfn(wn.VERB[clean_token].synsets())
        # if clean_token in wn.ADV:
        #         results+=adverbs(wn.ADV[clean_token].synsets())
        
        results+=relfn(wn.synsets(clean_token, pos=wn.NOUN))
        results+=adjectives(wn.synsets(clean_token, pos=wn.ADJ))
        results+=relfn(wn.synsets(clean_token, pos=wn.VERB))
        results+=adverbs(wn.synsets(clean_token, pos=wn.ADV))


        # try stemmed version
        # morphed_token=wn.morphy(clean_token, wn.NOUN)
        # if morphed_token!=None:
        #         if morphed_token in wn.NOUN:
        #                 results+=relfn(wn.NOUN[morphed_token].synsets())
        # morphed_token=wn.morphy(clean_token, wn.VERB)
        # if morphed_token!=None:
        #         if morphed_token in wn.VERB:
        #                 results+=relfn(wn.VERB[morphed_token].synsets())
        # morphed_token=wn.morphy(clean_token, wn.ADJ)
        # if morphed_token!=None:
        #         if morphed_token in wn.ADJ:
        #                 results+=adjectives(wn.ADJ[morphed_token].synsets())


        if results!=[]:
                # print(results)
                synset = results[random.randint(0,len(results)-1)]
                # print(synset)
                # shifted_token=synset[random.randint(0,len(synset)-1)]
                shifted_token = synset.name().split(".")[0]
                #shifted_token=synset[0]

        # print(clean_token, "-->", repr(results), shifted_token)
        # print("-->",)
        # print(repr(results))
        # print(shifted_token)

        return shifted_token

def mutateLine(line, relfn=sisters):
        pattern=r'''[A-Za-z]+|[0-9]+|[^\w\s]'''
        result=''
        first_space=''
        for token in regexp_tokenize(line, pattern):
            if(len(token)>2):
                mut_token = mutateWord(token, relfn)
                if token[0] in string.ascii_uppercase:
                    result+=first_space+string.capwords(mut_token.replace('_',' '))
                else:
                    result+=first_space+mut_token.replace('_',' ')
            elif token[0] in string.punctuation:
                result+=token
            else:
                result+=first_space+token
            if first_space=='':
                first_space=' '       

        return result

        
def checkWN(token):
        clean_token=token.lower()
        pos=''

        # try all parts of speech
        if clean_token in wn.NOUN:
                pos=pos+" (NOUN)"
        if clean_token in wn.ADJ:
                pos=pos+" (ADJ)"
        if clean_token in wn.VERB:
                pos=pos+" (VERB)"
        if clean_token in wn.ADV:
                pos=pos+" (ADV)"

        # try stemmed version
        morphed_token=wn.morphy(clean_token, wn.NOUN)
        if morphed_token!=None:
                if morphed_token in wn.NOUN:
                        pos+=" (NOUN when stemmed)"
        morphed_token=wn.morphy(clean_token, wn.VERB)
        if morphed_token!=None:
                if morphed_token in wn.VERB:
                        pos+=" (VERB when stemmed)"
        morphed_token=wn.morphy(clean_token, wn.ADJ)
        if morphed_token!=None:
                if morphed_token in wn.ADJ:
                        pos+=" (ADJ when stemmed)"                        
        if pos=='':
                #notinWN.append(clean_token)
                if clean_token not in nonWNwords:
                        nonWNwords[clean_token]=1
                else:
                        nonWNwords[clean_token]=nonWNwords[clean_token]+1
                
        else:
                #inWN.append(clean_token)
                if clean_token not in WNwords:
                        WNwords[clean_token]=1
                else:
                        WNwords[clean_token]=WNwords[clean_token]+1
                #inWN.append(clean_token+pos)
                

def file_len(fname):
    with open(fname, encoding = "ISO-8859-1") as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def parse_file(filename, wordfn=checkWN):
        print("opening "+repr(filename))

        print("file is {} lines".format(file_len(filename)))
        
        # had to add encoding on new macbook pro
        f=open(filename,  encoding = "ISO-8859-1")

        # look for properly formatted header:
        # two empty lines, followed by text, followed by two more empty lines
        double_newlines=0
        lastline=''
        
        for line in f:
                if line == '\n' and lastline=='\n':
                    double_newlines=double_newlines+1
                lastline=line
                if double_newlines==2:
                    #print "Found two double newlines"
                    break

        if double_newlines!=2:
            print("read entire file without finding appropriately formed header.  exiting.")
            exit

        print("parsing contents:")

        # split the rest of the file into lines
        pattern=r'''[A-Za-z]+|[0-9]+'''
        for line in f:
                for token in regexp_tokenize(line, pattern):
                    if len(token)>2:
                            if ignore(token.lower())==False:
                                    checkWN(token)


def walk_db(rootpath):
        for root, dirs, files in os.walk(rootpath, followlinks=True):

                local_base=os.path.basename(os.path.relpath(root,rootpath))

                pattern=r'''[A-Za-z]+'''
                for token in regexp_tokenize(local_base, pattern):
                        if(len(token)>2):
                                checkWN(token)

                for f in files: 
                        file_base=os.path.splitext(f)[0]
                        for token in regexp_tokenize(file_base, pattern):
                                if(len(token)>2):
                                        checkWN(token)

def main():  
        #parse_file('/Users/rtwomey/script/script.txt')                                                          
        #dbpath='/Volumes/Swimming Pool'
        #walk_db(dbpath)

        # parse index files for stats
##        parse_file('/Users/rtwomey/script/physical material.txt', checkWN)                                                          
##        parse_file('/Users/rtwomey/script/slightly more than shit.txt', checkWN)                                                          
##        parse_file('/Users/rtwomey/script/props.txt', checkWN)                                                          
##        parse_file('/Users/rtwomey/script/unassigned materials.txt', checkWN)

        # shift index file to sister terms
        parse_file('/Users/rtwomey/script/props.txt', mutateWord)
        parse_file('/Users/rtwomey/script/slightly more than shit.txt', mutateWord)

##        print "\n"
##        print "In WN:\n\n"+repr(WNwords)
##        print "\n"
##
##        print "\n"
##        print "Not in WN:\n\n"+repr(nonWNwords)
##        print "\n"

        #for key,val in nonWNwords.iteritems():
        #        print key,val

        #for key,val in WNwords.iteritems():
        #        print key,val

        print("\n")
        print("words in WN: "+str(len(WNwords)))
        print("\n")
        print("words not in WN: "+str(len(nonWNwords)))

if __name__ == '__main__':
        main()
