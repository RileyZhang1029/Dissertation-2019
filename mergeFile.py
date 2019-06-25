# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:21:03 2019

@author: Administrator
"""

 
import os 

n = 0
folder_out = os.getcwd() + "/testdata"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
with open("fileMerged_test.txt", 'w', encoding = "utf8") as f:
    os.chdir(folder_out)

    for txtFile in txtFiles:
        n += 1
        try:
            for line in open(txtFile, encoding = 'utf8'):
                f.writelines(line)
        except UnicodeDecodeError:
            print("error:" + txtFile)
            pass
        if n >= 10:
            break

  



