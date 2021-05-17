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
    #("/", "_"),
    ("\\", "_"),
    ("|", "_"),
    ("?", "_"),
    ("*", "_"),
    ]

filecount = 0
dircount = 0

for root, dirs, files in os.walk(directory, topdown=False):
    for file in files:
        newfile = file
        for c in chars:
            newfile = newfile.replace(c[0], c[1])
        if newfile != file:
            tempname = newfile; n = 0
            while os.path.exists(root+"/"+newfile):
                n = n+1; newfile = "dupe_"+str(n)+"_"+tempname
            shutil.move(root+"/"+file, root+"/"+newfile)
            print("renamed " + root + "/" + file + " to " + newfile)
            filecount+=1
    for dir in dirs:
        newdir = dir
        for c in chars:
            newdir = newdir.replace(c[0], c[1])
        if newdir != dir:
            print("renaming " + root + "/" + dir + " to " + newdir)
            shutil.move(root+"/"+dir, root+"/"+newdir)
            dircount+=1

print("Done!")
print("Renamed " + str(filecount) + " files")
print("Renamed " + str(dircount) + " dirs")
