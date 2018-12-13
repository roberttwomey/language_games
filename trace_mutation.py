#!/usr/bin/python
from WNutils import mutateWord
from WNutils import children, sisters, broadest
import sys
import warnings

warnings.simplefilter("ignore")

result=''
for arg in sys.argv[1:]:
    result+=mutateWord(arg, broadest).replace('_',' ')+' '

print result
