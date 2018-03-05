# genfind.py
#
# A function that generates files that match a given filename pattern

import os
# This module provides support for Unix shell-style wildcards, which are not the same as regular expressions
import fnmatch # Unix filename pattern matching

def gen_find(filepat,top):
    # filepat       : filename pattern
    for path, dirlist, filelist in os.walk(top):
        # path      : Current directory
        # dirlist   : List of subdirectories
        # filelist  : List of files
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)

# Example use

if __name__ == '__main__':
    lognames = gen_find("access-log*","www")
    for name in lognames:
        print(name)

# Linux system find / -name '*.py'