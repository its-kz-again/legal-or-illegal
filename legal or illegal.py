import re

def isLEGAL(line):
   if(re.findall("^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$",line)):
        return True
   return False

try:
    while True:
        line = input()
        x=isLEGAL(line)
        if x:
            print("LEGAL")
        else:
            print("ILLEGAL")
        #print(line)
except:
    pass