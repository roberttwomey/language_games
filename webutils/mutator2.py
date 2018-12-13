#!/usr/bin/python2.5

"""
An echo server that uses threads to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import cgi, cgitb
cgitb.enable()
import sys
sys.path.insert(0,"/home/rtwomey/nltk-0.9.7")
import WNutils
import warnings
from time import localtime, strftime
import os

def next_output_file(outpath):
    (base, extension)=os.path.splitext(outpath)
    timestamp=strftime("%Y%m%d", localtime())
    outfile=os.path.join(base+'_'+timestamp+'.txt')    
    return outfile

def main():
    # create instance of FieldStorage
    form = cgi.FieldStorage()

    # get data from the fields, if present
    query_str = form.getvalue('str')

    # avoid script injection
    query_str = cgi.escape(query_str)
    
    if query_str=="": query_str = "dog photo"
    input_phrase=query_str.replace("_", " ")

    # log current query string
    log_fname=next_output_file("logs/log.txt")
    out_f=open(log_fname, "a")
    out_f.write(strftime("%H:%M:%S\n", localtime()))
    out_f.write(input_phrase+" -> \n\n")

    
    # header
    print "Content-type: text/html\n\n"
    print "<html>\n<head>\n<title>WORD CHIPPER</title>\n"
    
    # javascript stuff

    print '''<link rel="stylesheet" type="text/css" href="jscroller2-1.0.css">'''
    print '''<link rel="stylesheet" type="text/css" href="../css/sitestyles.css">'''
    print '''<script type="text/javascript" src="jscroller2-1.5.js"></script>'''

    print "</script></head>"
    print '''<body class="bodytext">'''
    print "<p>&nbsp;</p>"
    print "<table class=\"bodytext\"><tr><td>"
    print """
<form name="input" action="mutator2.py">
<input type="text" name="str" size="20">
</form> -></td><td width="400">
"""
    print '''<div id="scroller_container">'''
    print ''' <div class="jscroller2_up jscroller2_speed-10 jscroller2_ignoreleave">'''
    i=1
    while i<10:
        result=WNutils.mutateLine(input_phrase, WNutils.sisters)
        print"<br> &nbsp;"+result+"<br>"
        out_f.write(result+"\n")
        i+=1
    result=WNutils.mutateLine(input_phrase, WNutils.sisters)    
    print "<br> &nbsp;"+result+"<br>"
    out_f.write(result+"\n\n")
    print "</div></div></td></tr></table>"  
    print "</body></html>"
    
if __name__ == "__main__":
    warnings.simplefilter("ignore")
    try:
        main()
    except:
        print "Content-type:text/html\n"
	print "<HTML>"
	print "<title>error?</title>"
	print "<body>"
	print "There was an error on the page<p/>"
	print "Notes;<br/>"
	print "</body>"
	print "</HTML>"

#EndOfFile

