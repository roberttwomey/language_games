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

def do_dvd_encode(path, filename):
    global webreadypath
    global dbpath
    
    outfile = os.path.join(webreadypath, path, "dvd_ws_"+os.path.splitext(filename)[0]+".mpg")
    if os.path.exists(outfile) == False:            
        print "encoding dvd compatible mpeg "
        infile = os.path.join(dbpath, path, filename).replace(' ','\ ')
        params = "-aspect 16:9 -target ntsc-dvd"
        try:
            retcode = call("ffmpeg -i "+infile+" "+params+" "+outfile.replace(' ','\ '), shell=True)
            #print "test "+ "ffmpeg -i "+infile+" "+params+" "+outfile.replace(' ','\ ')
        except OSError, e:
            print >>sys.stderr, "Execution failed:", e
            
def walk_db(rootpath):
        global dbpath
        print dbpath
        print webreadypath

        for root, dirs, files in os.walk(rootpath):

                localroot=os.path.relpath(root,dbpath)

                for f in files:
                        if os.path.splitext(f)[1] == '.mpg':
                            do_dvd_encode(localroot, f)

                        
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
