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
    if item[2].lower().replace(" ", "") not in item[3].lower().replace(" ", ""):
        print(item[0], item[2], item[3])
    articleList.append(item[0])
    st_men_all.append(item[2])
    articleDict.setdefault(item[0].lstrip("bioj:a"), []).append(item[2])
csvFile.close()

print("Howison length", len(set(articleList)))


st_men_all = sorted(set(st_men_all))
print(len(st_men_all))
# print(articleDict)
print(st_men_all)

st_men_all_new = [w for w in st_men_all if " " not in w and "-" not in w]
# print(st_men_all_new)
# print(len(st_men_all_new))



folder_out = os.getcwd() + "/testdata"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
txtFiles_nosupple = [f for f in txtFiles if "Supplemen" not in f]
# print("Text length", len(set(txtFiles_nosupple)))
os.chdir(folder_out)
for key, value in articleDict.items():
    for txtFile in txtFiles:
        flag = True
        if key == txtFile.strip(".txt"):
            document = open(txtFile, "r", encoding='utf-8').read()
            for v in value:
                if not document.lower().find(v.lower()):
                    print(v)
                    flag = False
            print(txtFile, flag)



