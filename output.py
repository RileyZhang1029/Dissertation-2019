# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:40:33 2019

@author: Administrator
"""

import csv

csvFile = open("results_each_article.csv", "r", encoding = "utf8")
reader = csv.reader(csvFile)
wordList = []

# with open("/home/riley/Documents/Github/Dissertation-2019/Prodigy/output.txt", 'w', encoding = "utf8") as f:
#     for item in reader:
#         if reader.line_num == 1:
#             continue
#         if item[2].lower().replace(" ", "") in item[3].lower().replace(" ", ""):
#             wordList.append(item[2])
#             f.write(item[3].replace("\n", " "))
#             f.write("\n")
#
#
# with open("/home/riley/Documents/Github/Dissertation-2019/Prodigy/output_word.txt", 'w', encoding = "utf8") as j:
#     for w in set(wordList):
#         if " " in w:
#             j.write("{\"label\":\"SOFTWARE\",\"pattern\":[{\"lower\":\"")
#             j.write(w.lower())
#             j.write("\"}]}")
#             j.write("\n")



with open("/home/riley/Documents/Github/Dissertation-2019/Prodigy/st_patterns_395.jsonl", 'w', encoding = "utf8") as f:
    for item in reader:
        if reader.line_num == 1:
            continue
        wordList.append(item[2])
    for w in set(wordList):
        if ' ' not in w:
            f.write("{\"label\":\"SOFTWARE\",\"pattern\":[{\"lower\":\"")
            f.write(w.lower())
            f.write("\"}]}")
            f.write("\n")
print(len(set(wordList)))


csvFile.close()