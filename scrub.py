#!/usr/bin/env python3
import os
import shutil
import sys

directory = sys.argv[1]

chars = [
    ("<", "_"),
    (">", "_"),
    (":", "_"),
    ('"', "_"),
    ("/", "_"),
    ("\\", "_"),
    ("|", "_"),
    ("?", "_"),
    ("*", "_"),
    ]

for root, dirs, files in os.walk(directory):
    for file in files:
        newfile = file
        for c in chars:
            newfile = newfile.replace(c[0], c[1])
        if newfile != file:
            tempname = newfile; n = 0
            while os.path.exists(root+"/"+newfile):
                n = n+1; newfile = "dupe_"+str(n)+"_"+tempname
            shutil.move(root+"/"+file, root+"/"+newfile)

for index, dir in enumerate(directory):
    newdir = dir
    for c in chars:
        newdir = newdir.replace(c[0], c[1])
    if newdir != dir:
        tempname = newdir; n = 0
        while os.path.exists(root+"/"+newdir):
            n = n+1; newdir = "dupe_"+str(n)+"_"+tempname
        shutil.move(root+"/"+dir, root+"/"+newdir)
        dirs[index] = newdir