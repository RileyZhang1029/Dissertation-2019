# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:21:03 2019

@author: Administrator
"""

 
import os 


folder_out = os.getcwd() + "/trainingdata_labelled"
n = 0
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
print(len(txtFiles))
with open("fileMerged_labelled.txt", 'w', encoding = "utf8") as f:
    os.chdir(folder_out)
    for txtFile in txtFiles:
        #遍历单个文件，读取行数
        n = n+1
        try:
            for line in open(txtFile, encoding = 'utf8'):
                f.writelines(line)
        except UnicodeDecodeError:
            print("error:" + txtFile)
            pass
        if n >= 40:
            break
print(n)
                
  



