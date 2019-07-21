import csv
import os
import re

csvFile = open("results_each_article.csv", "r")
reader = csv.reader(csvFile)
articleList = []
articleDict = {}
st_men_all = []

for item in reader:
    if reader.line_num == 1:
        continue
    articleList.append(item[0])
    st_men_all.append(item[2])
    articleDict.setdefault(item[0].lstrip("bioj:a"), []).append(item[2])
csvFile.close()

print("Howison length", len(set(articleList)))

print(len(st_men_all))
st_men_all = sorted(set(st_men_all))
print(len(st_men_all))
print(articleDict)


folder_out = os.getcwd() + "/test"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
txtFiles_nosupple = [f for f in txtFiles if "Supplemen" not in f]
print("Text length", len(set(txtFiles_nosupple)))
os.chdir(folder_out)
for key, value in articleDict.items():
    for txtFile in txtFiles:
        flag = True
        if key == txtFile.strip(".txt"):
            document = open(txtFile, "r", encoding='utf-8').read()
            for v in value:
                if not document.lower().find(v.lower()):
                    flag = False
            print(txtFile, flag)



