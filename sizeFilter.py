# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:21:03 2019

@author: Administrator
"""
import os
import re

n = 0
x = 0

folder_out = os.getcwd() + "/trainingdata"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]

os.chdir(folder_out)
for txtFile in txtFiles:

    count = 0
    textsize = round(os.path.getsize(txtFile)/float(1024), 2)
    # print(textsize)
    with open(txtFile, 'r') as f:
        dictResult = {}

        # Find the letters each line
        for line in f.readlines():
            listMatch = re.findall('[0-9]+', line)

            # Count
            for eachLetter in listMatch:
                eachLetterCount = len(re.findall(eachLetter, line))
                count += eachLetterCount



    if textsize >=10 and count <= 900:
        x += 1
    else:
        os.remove(os.path.join(folder_out, txtFile))
        os.remove(os.path.join(folder_out, txtFile.replace("txt","pdf")))


print(x)





