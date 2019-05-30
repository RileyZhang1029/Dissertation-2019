# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:21:03 2019

@author: Administrator
"""

#os模块中包含很多操作文件和目录的函数 
#os.getcwd()+'\trainingdata'   获取当前路径
 
import os 

folder_out = "C:/Users/Administrator/Documents/GitHub/Dissertation-2019/pdf_articles/pdf2txt"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
print(len(txtFiles))

with open("C:/Users/Administrator/Documents/GitHub/Dissertation-2019/pdf_articles/fileMerged.txt", 'w', encoding = "utf8") as f:
    for txtFile in txtFiles:
        #遍历单个文件，读取行数 
        try:
            for line in open(txtFile, encoding = 'utf8'):
                f.writelines(line.replace('\n',''))  
#                    f.write('\n')
        except UnicodeDecodeError:
            print("error:" + txtFile)
            pass
                
  



