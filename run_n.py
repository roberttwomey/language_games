from WNutils import mutateWord
from WNutils import children
from WNutils import sisters
import sys
import warnings

warnings.simplefilter("ignore")

result=''

if sys.argv[1] == 'children':
    print "looking for children"
    relfn=children
else:
    print "looking for sisters"
    relfn=sisters

out_f=open("logs/log.txt", "a")

out_f.write('\n')
for arg in sys.argv[3:]:
    out_f.write(arg+' ')
out_f.write('->\n')

i=0
while i < int(sys.argv[2]):
    result=''
    for arg in sys.argv[3:]:
        result+=mutateWord(arg, relfn).replace('_',' ')+' '
    i+=1
    print result
    out_f.write(result+"\n")

out_f.close()
