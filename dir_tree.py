# Implement a program dir_tree.py that takes a directory as argument and prints all the files
# in that directory recursively as a tree.
# Hint: Use os.listdir and os.path.isdir functions.
from os import listdir, walk
from os.path import isfile, isdir, join
import sys

dir = sys.argv[1]
 
def directory(dir):
    for f in listdir(dir):
        if(isdir(join(dir,f))):
            directory(join(dir,f))
        else:
            print(join(dir,f))
        
directory(dir)
