# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:40:33 2019

@author: Administrator
"""

import csv

csvFile = open("results_each_article.csv", "r", encoding = "utf8")
reader = csv.reader(csvFile)

with open("output.txt", 'w', encoding = "utf8") as f:
    for item in reader:
        if reader.line_num == 1:
            continue
        f.write(item[3].replace("\n", " "))
        f.write("\n")