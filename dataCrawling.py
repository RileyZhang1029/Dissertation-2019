# -*- coding: utf-8 -*-
"""
Created on Wed May 29 23:30:10 2019

@author: Administrator
"""
import time
import csv
import os
import urllib
import posixpath
import urllib.parse 


start = time.clock()
direc = os.getcwd()+"\\trainingdata1" 
if not os.path.exists(direc):
    os.makedirs(direc)


n = 0
filename = "C:/Users/Administrator/Documents/GitHub/Dissertation-2019/oa_non_comm_use_pdf.csv"
with open(filename,'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if(row[1].find("Bioinformatics") != -1):
            n += 1
            if n>417:
                print(n, row[1])
                pdf_url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/" + row[0]
    
                path = urllib.parse.urlsplit(pdf_url).path
                filename = posixpath.basename(path)
    
                save_path = os.path.join(direc, filename)
                urllib.request.urlretrieve(pdf_url , save_path)
            
#        if(n>=2):
#            break
            
print(n)
            
end = time.clock()
totaltime = end-start
print("Time used:", totaltime)