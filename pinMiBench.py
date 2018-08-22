#! /usr/bin/env python
import sys
import os
import fileComsoft




def main():
    pinTool=sys.argv[1]
    mibenchDir=sys.argv[2]
    fileNames=sys.argv[3].split('|')
    for i in range(len(fileNames)):
        fileNames[i] = fileNames[i].lower()
    matchList=[]
    fileComsoft.search(mibenchDir, fileNames, matchList)
    
    if matchList.count == 0:
        print('no specified file name is found!')
    else:        
        print(str(len(matchList)) + ' files found!')
        for i in range( len(matchList)):
            print i+1, matchList[i]
            
        for f in matchList:
            #1. change working directory
            os.chdir(os.path.dirname(f))
                        
            #2. execute             
            cmd = fileComsoft.findMiBenchCmd(f)
            fileComsoft.pinCmd(pinTool, cmd)    
            
            

main()

#with open(sys.argv[1], 'r') as f:
 #   for line in f:
  #      print(line)
