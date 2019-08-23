# -*- coding: utf-8 -*-
"""
B134977
Crawl training data through urls.
link to the Github Repostory: https://github.com/RileyZhang1029/Dissertation-2019
"""

import time
import csv
import os
import posixpath
import urllib.parse 


start = time.clock()
direc = os.getcwd()+"/trainingdata"
if not os.path.exists(direc):
    os.makedirs(direc)


n = 0
filename = "path/to/oa_non_comm_use_pdf.csv"
with open(filename,'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if(row[1].find("Bioinformatics") != -1):
            if n < 400:
                n += 1
                print(n, row[1])
                pdf_url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/" + row[0]

                path = urllib.parse.urlsplit(pdf_url).path
                filename = posixpath.basename(path)

                save_path = os.path.join(direc, filename)
                urllib.request.urlretrieve(pdf_url , save_path)
            
print(n)
end = time.clock()
totaltime = end-start
print("Time used:", totaltime)