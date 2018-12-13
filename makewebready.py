#!/usr/local/bin/python
#
# Utils to take a directory structure of images, text, etc., and prepare
# it to be a dynamically displayed website:
# --makes lower resolution versions of images
# --makes thumbnails for video files

from nltk.tokenize import regexp_tokenize
import os
from subprocess import call
import sys

webreadypath=""
dbpath=""

def makethumbnail(path, filename):
    global webreadypath
    global dbpath

    # convert DSC02809.JPG -quality 75 -sample 150x150
    # /Volumes/Swimming\ Pool/web/DSC02809.t.jpg
    
    outfile = os.path.join(webreadypath, path, os.path.splitext(filename)[0]+".t.jpg")
    if os.path.exists(outfile) == False:   
        print "creating thumbnail "
        infile = os.path.join(dbpath, path, filename).replace(' ','\ ')
        params = "-quality 50 -geometry 150x150"
        try:
            retcode = call("convert"+" "+infile+" "+params+" "+outfile.replace(' ','\ '), shell=True)
        except OSError, e:
            print >>sys.stderr, "Execution failed:", e

def makemedium(path, filename):
    global webreadypath
    global dbpath
    
    #convert DSC02809.JPG -quality 75 -sample 800x800
    #  /Volumes/Swimming\ Pool/web/DSC02809.t.jpg
    outfile = os.path.join(webreadypath, path, os.path.splitext(filename)[0]+".jpg")
    if os.path.exists(outfile) == False:            
        print "creating medium res "
        infile = os.path.join(dbpath, path, filename).replace(' ','\ ')
        params = "-quality 60 -geometry 800x800"
        try:
            retcode = call("convert"+" "+infile+" "+params+" "+outfile.replace(' ','\ '), shell=True)
        except OSError, e:
            print >>sys.stderr, "Execution failed:", e
                           
def makeimages(path, filename):
    print os.path.join(path, filename)
    makethumbnail(path, filename)                           
    makemedium(path, filename)

def makedir(path):
    global webreadypath
    outpath=os.path.join(webreadypath, path)
    #print "checking "+outpath
    if os.path.exists(outpath) == False:
        print "making dir"
        os.makedirs(outpath)

def walk_db(rootpath):
        global dbpath
        print dbpath
        print webreadypath

        for root, dirs, files in os.walk(rootpath):

                localroot=os.path.relpath(root,dbpath)

                for f in files:
                        f_ext = os.path.splitext(f)[1]
                        if f_ext == '.jpg' or f_ext == '.JPG' or f_ext == '.tif' or f_ext == '.bmp':
                            makedir(localroot)
                            makeimages(localroot, f)
                        
def main():  
        global webreadypath
        global dbpath

        if len(sys.argv)<3:
		print "usage: makewebready.py /path/to/input /path/to/output\n"
	else:
		print "walking "+sys.argv[1]
		dbpath=sys.argv[1]
		webreadypath=sys.argv[2]
		walk_db(dbpath)
	
if __name__ == '__main__':
        main()
