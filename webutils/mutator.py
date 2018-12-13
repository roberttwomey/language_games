#!/usr/bin/python2.5

"""
An echo server that uses threads to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import sys
sys.path.insert(0,"/home/rtwomey/nltk-0.9.7")
import WNutils
import warnings
import cgi, cgitb

def main():
    # create instance of FieldStorage
    form = cgi.FieldStorage()

    # get data from the fields, if present
    query_str = form.getvalue('str')
    if query_str=="": query_str = "dog photo"
    input_phrase=query_str.replace("_", " ")
    
    # header
    print "Content-type: text/html\n\n"
    print "<html>\n<head>\n<title>"+input_phrase+"</title>\n"
    
    # javascript stuff

    print '''<script type="text/javascript" src="scroll.js"></script>'''

    print "</script></head>"
    print "<body>"

    print "<table><tr><td>"
    print input_phrase+"</td><td>"
    print '''<div id="names" onmousemver="recScroll('names'),'up', 1);">'''
    i=1
    while i<20:
        print"<br> &nbsp;"+WNutils.mutateLine(input_phrase, WNutils.sisters)+"<br>"
        i+=1
    print "<br> &nbsp;"+WNutils.mutateLine(input_phrase, WNutils.sisters)+"<br>"
    print "</td></tr></table>"

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

