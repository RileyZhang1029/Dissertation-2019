import csv
import os
import random
import difflib


folder_out = os.getcwd() + "/testdata"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]


def get_equal_rate_1(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()



word_list = []
item2_list = []
no_list = []
csvFile = open("results_each_article.csv", "r")
reader = csv.reader(csvFile)
n=0
os.chdir(folder_out)

for item in reader:
    if reader.line_num == 1:
        continue
    item2_list.append(item[3])
    for txtFile in sorted(txtFiles):
        for line in open(txtFile, encoding = 'utf8'):
            if item[0].replace('bioj:a', '') in txtFile:
                if item[2] != 'O' and item[2] != 'R':
                    if item[2].lower() in line.lower():
                        if get_equal_rate_1(line, item[3]) > 0.8:
                            n += 1
                            no_list.append(line)
                            word_list.append(item[3])
                            # print(item[2])
                            # print(txtFile, ':', item[3])
                            # print(txtFile, ':', line)
                    # else:
                        # print(item[2])
                        # print(txtFile, ':', item[3])
                        # print(txtFile, ':', line)




csvFile.close()


print(n)
worddiff = [w for w in item2_list if w not in word_list]
# print(worddiff)
# print(len(item2_list))
with open("/home/riley/Documents/Github/Dissertation-2019/Prodigy/fileMerged_test.txt", 'w', encoding = "utf8") as f:
    for txtFile in sorted(txtFiles):
        for line in open(txtFile, encoding = 'utf8'):
            if line not in no_list:
                f.writelines(line)

for w in worddiff:
    print(w)
