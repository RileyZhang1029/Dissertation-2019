# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:21:03 2019

@author: Administrator
"""

 
import os
import random

n = 0
folder_out = os.getcwd() + "/trainingdata395"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
with open("/home/riley/Documents/Github/Dissertation-2019/Prodigy/fileMerged_new395.txt", 'w', encoding = "utf8") as f:
    os.chdir(folder_out)

    # random.shuffle(txtFiles)
    print(len(txtFiles))

    # for i in range(200):
    #     # print(txtFiles[i])
    #     try:
    #         for line in open(txtFiles[i], encoding = 'utf8'):
    #             f.writelines(line)
    #
    #     except UnicodeDecodeError:
    #         print("error:" + txtFiles[i])
    #         pass

    try:
        for txtFile in sorted(txtFiles):
            print(txtFile)
            for line in open(txtFile, encoding = 'utf8'):
                f.writelines(line)

    except UnicodeDecodeError:
        print("error:" + txtFile)
        pass

  


  



