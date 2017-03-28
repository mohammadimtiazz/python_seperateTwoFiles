# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:15:11 2017

@author: Mohammad Imtiaz
"""

import os

#here the firectories have two different file sets
# 1. flastIris
# 2. flastMask
# The purpose is to seperate these two files into two different folders


#destion where the file will be moved
#This directory have to be created before executing this program
destination = 'D:\EyeLock Projects\Anti-spoofing\Spoof\GL_flastIrisMask\GL_flatIris\\'
textCheck = 'FlatMask.pgm'    #compare the existing file set with this filename
textCheck = list(textCheck)

#copy all file directory in content
with open('fileName.txt') as f:     #save directories in 'fileName.txt' of all files
    content = f.readlines()

for i in xrange(0, len(content)):
#for i in xrange(0, 4):
    strX = content[i]       # strX contain each file directory
    
    textSave = []       

    #save string before _
    v = 1
    while (strX[len(strX) - v - 1] is not '_'):
        textSave.append(strX[len(strX) - v - 1] )
        v += 1
    
    textSave.reverse()

    
    #Compare string saved in textCheck with testsave
    v = 0
    checker = True 
    if len(textCheck) == len(textSave):
        for i in xrange(0, len(textSave)):
            if textSave[i] is not textCheck[i]:
                checker = False
    
    #save source dir
    source = strX[0:len(strX) - 1]
    
    #modified destination directory
    destinationX = []
    if checker:
        pass
    else:
        v = 1
        while (strX[len(strX) - v - 1] != '\\'):
            destinationX.append(strX[len(strX) - v - 1] )
            v += 1
    
        destinationX.reverse()
        destinationX = ''.join(destinationX)
        destinationMod = destination + str(destinationX)
        
        os.rename(source, destinationMod)
    
    del textSave, destinationX, source