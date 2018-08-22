#! /usr/bin/env python
import sys
import os

import fileComsoft


'''
usage: build.py benchmark_dir make_file
example: build.py ~/MiBench Makefile
'''
def main():
    mibenchDir=sys.argv[1]
    fileNames=sys.argv[2].split('|')
    for i in range(len(fileNames)):
        fileNames[i] = fileNames[i].lower()
    matchList=[]
    fileComsoft.search(mibenchDir, fileNames, matchList)
    
    if matchList.count == 0:
        print('no ' + fileName + ' is found!')
    else:        
        print(str(len(matchList)) + ' files found!')
        for i in range( len(matchList)):
            print i+1, matchList[i]
        for f in matchList:
            os.chdir(os.path.dirname(f))
            #1. make first
            #
            print("===Compiling " + os.path.dirname(f) + " ===")
            print os.popen("make").read()         
           

main()
            


#with open(sys.argv[1], 'r') as f:
 #   for line in f:
  #      print(line)
