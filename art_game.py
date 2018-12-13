# ArtGame.py
#
# by:
# robert.twomey@gmail.com
#
# additional content by:
# not_robert@roberttwomey.com
#
# Short interactive shell program:
# to take input at command prompt
# and return a semantically altered version

import WNutils
import sys
import warnings
from IndexFile import IndexFile
from time import localtime, strftime
import os

winning_lines=[]
current=[]
out_f = ""
mut_line = []

prompt_phrases=[ "Is my idea better than yours?",
                 "Have I distracted you yet?" ]

def check_input(line):
        global mut_line
        mut_line=WNutils.mutateLine(line, WNutils.broadest)
        print mut_line
##        print "My idea:> "+mut_line
##        i=0;
##        while i < 10:
##            mut_line=WNutils.mutateLine(line, WNutils.broadest)
##            print "Another one:> "+mut_line
##            i+=1
##        current=mut_line
        #out_f.write('\n'+line+' ->\n')
        #out_f.write(mut_line+'\n')
        #out_f.flush()

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

def verify_success():
    query=raw_input("\nIs my idea better than yours? (y/n) ")
    if query=='y':
        return True
    else:
        return False

def verify_play_again():
    query=raw_input("\nplay again? (y/n)")
    if query=='y':
        return True
    else:
        return False
    
def main():
    #global out_f
    warnings.simplefilter("ignore")

    #fname=next_output_file("logs/log.txt")
    #out_f=open(fname, "a")
    os.system('clear')
    print('''
        ========================================================
              ___           ___           ___     
             /\  \         /\  \         /\  \    
            /::\  \       /::\  \        \:\  \   
           /:/\:\  \     /:/\:\  \        \:\  \  
          /::\~\:\  \   /::\~\:\  \       /::\  \ 
         /:/\:\ \:\__\ /:/\:\ \:\__\     /:/\:\__\ 
         \/__\:\/:/  / \/_|::\/:/  /    /:/  \/__/
              \::/  /     |:|::/  /    /:/  /     
              /:/  /      |:|\/__/     \/__/      
             /:/  /       |:|  |                  
             \/__/         \|__|                  
              ___           ___           ___           ___     
             /\  \         /\  \         /\__\         /\  \    
            /::\  \       /::\  \       /::|  |       /::\  \   
           /:/\:\  \     /:/\:\  \     /:|:|  |      /:/\:\  \  
          /:/  \:\  \   /::\~\:\  \   /:/|:|__|__   /::\~\:\  \ 
         /:/__/_\:\__\ /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:\__\ 
         \:\  /\ \/__/ \/__\:\/:/  / \/__/~~/:/  / \:\~\:\ \/__/
          \:\ \:\__\        \::/  /        /:/  /   \:\ \:\__\  
           \:\/:/  /        /:/  /        /:/  /     \:\ \/__/  
            \::/  /        /:/  /        /:/  /       \:\__\    
             \/__/         \/__/         \/__/         \/__/    
        ========================================================
        :: I HAVE MORE IDEAS THAN YOU                         ::
        ========================================================
''')
    
    line=""
    play_again=True
    my_score=0
    your_score=0
    while play_again==True:
        line=raw_input("Your Idea:>")
        if len(line) > 0:
            print("My idea:")
            check_input(line)
            done=False
            while done != True:
                done=verify_success()
                print(" ")
                if done != True:
                    print("OK, how about this:")
                    check_input(line)
            my_score+=1
            winning_lines.append(mut_line)
        print("score: Me %s, you %s" % (my_score, your_score))
        play_again=verify_play_again()
    print("Winning lines:")
    print("Me:")
    for l in winning_lines:
            print l
    print("You:")
    print("")
    print("\nThanks for playing!\n")
    
        
if __name__ == '__main__':
    main()
    

