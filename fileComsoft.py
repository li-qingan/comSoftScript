#! /usr/bin/env python
import sys
import os


#find the first filename of each subPath
def search(curpath, filenames, matchList):
    L = os.listdir(curpath)    
    for subPath in L:
        fullPath = os.path.join(curpath, subPath)
        if os.path.isdir(fullPath):
            search(fullPath, filenames, matchList)
        elif os.path.isfile(fullPath):
            if subPath.lower() in filenames:
                 matchList.append(fullPath)
                 return    
    return

def searchSuffix(curPath, suffixes, matchList):
    L = os.listdir(curPath)    
    for subPath in L:
        fullPath = os.path.join(curPath, subPath)
        if os.path.isdir(fullPath):
            searchSuffix(fullPath, suffixes, matchList)
        elif os.path.isfile(fullPath):
            slices = os.path.splitext(subPath)
            if slices[1] in suffixes:
                 matchList.append(fullPath)
                 return    
    return

def addRelPath(cmd):
    if cmd.find('./') != 0:
        return './' + cmd
    else:
        return cmd

'''
parse runme_small.sh or runme_large.sh or runme.sh
'''
def findMiBenchCmd(file):
    with open(file, 'r') as fstream:
        lines=fstream.readlines()
        cmd=lines[1].strip()             
        #if there is 'cd' command, real cmd is expected next
        if cmd.find('cd ') == 0:
            path=cmd[3:].strip()
            os.chdir(os.path.abspath(path))
            cmd=addRelPath(lines[2])
        else:
            cmd = addRelPath(cmd)
    return cmd

def pinCmd(pinTool, cmd):
    #find pin_path from environmental variables
    env_dist=os.environ
    pinPath=env_dist.get('PIN_PATH')
    pin=os.path.join(pinPath, 'pin')
    pinTool=os.path.join(pinPath, 'source/tools/comsoft/obj-ia32', pinTool)+'.so'
    
    pinCmd=pin+' -t '  + pinTool + ' -- ' + cmd
    print('Executing ' + pinCmd)
    print os.popen(pinCmd).read()
    
    return

'''
parse README.exec_info or exec_info files in each app
'''
def findMediaBenchCmd(fileName):
    appDir = os.path.dirname(fileName)
    file= open(fileName, 'r')
    lines = file.readlines()
    cmdLine = ''
    replacement = ''
    for line in lines:
        #skip empty lines
        if len(line.strip()) == 0:
            continue
        #skip non-indent lines
        elif len(line.lstrip()) == len(line):
            words = line.split(' ')
            if words[0] == 'Assuming':
                replacement = words[3]
            continue
        else:
            cmdLine = line
            break
    #revise exec-cmd
    
    execInfos = cmdLine.split(' ')
    if execInfos.count == 0:
        print('Error parsing exec infos!')
        cmd = ''
    else:    
        if len(replacement) > 0:
            execInfos[0] = replacement
        else:
            execInfos[0] = execInfos[0].strip()
        #revise output|input path
        for i in range(len(execInfos)):
            if execInfos[i].find('input_base') == 0:
                execInfos[i] = os.path.join('./input_base', execInfos[i])
            elif execInfos[i].find('output_base') == 0:
                execInfos[i] = os.path.join('./output_base', execInfos[i])
            else:
                pass
       
        execfileList=[]
        search(appDir, execInfos[0], execfileList)            
        if len(execfileList) < 1:
            print "=====Error:\tcan't find exec file:\t" + cmdArgs[0] + " in " + appDir
        else:
            execInfos[0]=execfileList[0]
            cmd = " ".join(execInfos)         
    return cmd