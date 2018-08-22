#! /usr/bin/env python
import sys
import os
import fileComsoft



def run(pardir, cmds): 
   
    print('Executing ' + cmds)        
    print os.popen(cmds).read()
    
    
    #print('======Executing: ' + pardir + ":" + cmd)
    #print os.popen(cmd).read()
    #outf = os.popen(cmd)
    #outs = outf.read()
   # print outs   
    return


'''
usage: run.py benchmark_dir runme_small.sh
example: run.py ~/MiBench runme_small.sh
'''

def main():
    mibenchDir=sys.argv[1]
    fileNames=sys.argv[2].split('|')
    for i in range(len(fileNames)):
        fileNames[i] = fileNames[i].lower()
    matchList=[]
    
    fileComsoft.search(mibenchDir, fileNames, matchList)
    
    if matchList.count == 0:
        print('no specified files is found!')
    else:        
        print(str(len(matchList)) + ' files found!')
        for i in range( len(matchList)):
            print i+1, matchList[i]
        for f in matchList:
            #1. change working directory
            os.chdir(os.path.dirname(f))
                        
            #2. execute cmd            
            cmd=fileComsoft.findMiBenchCmd(f)                    
            run(os.path.dirname(f), cmd)    
            
            

main()

#with open(sys.argv[1], 'r') as f:
 #   for line in f:
  #      print(line)
