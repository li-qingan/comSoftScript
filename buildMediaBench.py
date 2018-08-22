#! /usr/bin/env python
import sys
import os

import fileComsoft


'''
Building MediaBench consists three steps:
1) tar xf  .gz|.tgz files or unzip .zip files
2) configure
3) make
usage: build.py benchmark_dir suffix
example: build.py ~/MiBench .gz|.zip|.tgz
'''
def main():
    mibenchDir=sys.argv[1]
    suffixes=sys.argv[2].split('|')
    for i in range(len(suffixes)):
        suffixes[i] = suffixes[i].lower()
    matchList=[]
    fileComsoft.searchSuffix(mibenchDir, suffixes, matchList)
    
    if matchList.count == 0:
        print('no ' + fileName + ' is found!')
    else:        
        print(str(len(matchList)) + ' files found!')
        for i in range( len(matchList)):
            print i+1, matchList[i]
        for f in matchList:
            os.chdir(os.path.dirname(f))
            
            #1. tar xf or unzip dv  
            # check whether is decompressed. If so, pass
            slice = os.path.splitext(f)
            if os.path.isdir(slice[0]) :
                print slice[0] + ' already exist!'
                continue
            
                      #
            if f.endswith('.gz') or f.endswith('.tgz'):
                cmd = 'tar xf ' + f + ' --skip-old-files '
            elif f.endswith('.zip'):
                cmd = 'unzip -q -n ' + f 
                    
            print("===DeCompressing " + f + " ===")
            print cmd
            print os.popen(cmd).read()
            
            #2. configure
            configureFiles = []
            fileComsoft.search(os.getcwd(), 'configure', configureFiles )
            for conf in configureFiles:
                os.chdir(os.path.dirname(conf))
                # check whether is confugured. If so, pass
                makefiles = []
                fileComsoft.search(os.path.dirname(conf), 'makefile', makefiles)
                if makefiles.count > 0 :
                    print os.path.dirname(conf) + ' already configured!'
                    continue
                
                cmd = './configure'
                print cmd
                print os.popen(cmd).read()
                
            #3. make
            makeFiles = []
            fileComsoft.search(os.getcwd(), 'makefile', makeFiles )
            for conf in makeFiles:
                os.chdir(os.path.dirname(conf))
                cmd = 'make'
                print '========== ' +  cmd + ' in ' + os.path.dirname(conf)
                print os.popen(cmd).read()    

main() 
            
            


#with open(sys.argv[1], 'r') as f:
 #   for line in f:
  #      print(line)
