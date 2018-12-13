import time, os
import glob
import random

log_file_list=[]
playback_file = None
filenum = 0

def newest_file():
    root = 'logs/' # one specific folder

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

def make_logfile_lists():
    global log_file_list
    
    root = 'logs/' # one specific folder
    log_file_list = []
    for folder in glob.glob(root):
        for file in glob.glob(folder + '/*.txt'):
            log_file_list.append(file)

def print_next_idle_line():
    min_sleep=7
    max_sleep=10
    line=""
    while line != '\n':
        line=playback_file.readline()
        if line=="":
            cycle_next_playback_file()
            print(" ")
        else:
            print line,
    time.sleep(random.randint(min_sleep, max_sleep))
        
def open_playback_file(filename):
    global playback_file
#    playback_file = open("logs/log_20090214_4.txt","r")   
    playback_file = open(filename,"r")

def cycle_next_playback_file():
    global playback_file
    global filenum
    global log_file_list
    playback_file.close()

    filenum+=1
    if filenum > len(log_file_list):
        filenum=0
    open_playback_file(log_file_list[filenum])
    
def main():
    global log_file_list
    
    random.seed()
    os.system('clear')
       
    make_logfile_lists()
    random.shuffle(log_file_list)
    #print repr(log_file_list)
    open_playback_file(log_file_list[0])
    
    filename = newest_file()
    
    idletime=0
    idlemode=False
    start_idling=20
    
    while 1:
        restart=False       
        #Set the filename and open the file
        #filename = './logs/log_20090214_4.txt'
        in_file = open(filename,'r')

        #Find the size of the file and move to the end
        st_results = os.stat(filename)
        st_size = st_results[6]
        in_file.seek(st_size)

        while restart==False:
            where = in_file.tell()
            line = in_file.readline()
            if not line:
                time.sleep(1)
                in_file.seek(where)

                idletime+=1
                if idletime>start_idling:
                    idlemode=True
                if idlemode:
                    print_next_idle_line()
            else:
                idletime=0
                idlemode=False
                cycle_next_playback_file()
                print line, # already has newline
            new_file = newest_file()
            if new_file != filename:
                filename=new_file
                log_file_list.append(filename)
                restart=True
        in_file.close()
    
if __name__ == '__main__':
    main()
