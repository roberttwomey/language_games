from WNutils import mutateWord
from WNutils import children
import sys
import warnings

warnings.simplefilter("ignore")

result=''
out_f=open("logs/log.txt", "a")
out_f.write("mutate ")
for arg in sys.argv[1:]:
    result+=mutateWord(arg, children).replace('_',' ')+' '
    out_f.write(arg)

out_f.write('\n')
#print "try: "+result
print result

out_f=open("logs/log.txt", "a")
out_f.write(result+"\n")
out_f.close()
