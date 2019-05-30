# -*- coding: utf-8 -*-
"""
Created on Wed May 29 23:30:10 2019

@author: Administrator
"""


import os
import urllib
import posixpath
import urllib.parse 
import time 


start = time.clock()
direc = os.getcwd()+"\\trainingdata" 
if not os.path.exists(direc):
    os.makedirs(direc)


n = 0
textname = "C:/Users/Administrator/Documents/GitHub/Dissertation-2019/oa_non_comm_use_pdf.txt"
with open(textname,"r") as file:
    lines = file.readlines()
    for line in lines:
        if(line.find("bio") != -1):
            n += 1
            print(n, line.split()[0])
            pdf_url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/" + line.split()[0]

            path = urllib.parse.urlsplit(pdf_url).path
            filename = posixpath.basename(path)

            save_path = os.path.join(direc, filename)
            urllib.request.urlretrieve(pdf_url , save_path)
            
        if(n>=600):
            break
            
#print(n)
            
end = time.clock()
totaltime = end-start
print("Time used:", totaltime)