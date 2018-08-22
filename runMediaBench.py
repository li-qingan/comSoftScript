#! /usr/bin/env python
import sys
import os
import fileComsoft



'''
Building MediaBench consists three steps:
1) tar xf  .gz|.tgz files or unzip .zip files
2) configure
3) make

usage: run.py benchmark_dir run_config
example: run.py ~/MediaBench README.exec_info
'''
def main():
    benchDir=sys.argv[1]
    execInfoName=sys.argv[2].split('|')
    for i in range(len(execInfoName)):
        execInfoName[i] = execInfoName[i].lower()
    #find exec_info files
    execInfoFiles=[]
    fileComsoft.search(benchDir, execInfoName, execInfoFiles )   
    
    
    if execInfoFiles.count == 0:
        print('no specified files is found!')
    else:        
        print(str(len(execInfoFiles)) + ' files found!')
        for i in range(len(execInfoFiles)):
            print i+1, execInfoFiles[i]
        for f in execInfoFiles:
            
            #1. change working directory
            os.chdir(os.path.dirname(f))
            appDir=os.getcwd()
            #2. find exec files via exec_info files
            cmd = fileComsoft.findMediaBenchCmd(f)
                            
            print('=====Executing ' + cmd)        
            print os.popen(cmd).read()

main()
            
            


#with open(sys.argv[1], 'r') as f:
 #   for line in f:
  #      print(line)
