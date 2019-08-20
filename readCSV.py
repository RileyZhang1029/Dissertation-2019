import csv
import os
import random

csvFile = open("results_each_article.csv", "r")
reader = csv.reader(csvFile)
articleList = []
articleDict = {}
st_men_all = []
st_men_multi = []
senList = []
senList_nomulti = []

for item in reader:
    if reader.line_num == 1:
        continue
    # if item[2].lower().replace(" ", "") not in item[3].lower().replace(" ", ""):
        # print(item[0], item[2], item[3])
    articleList.append(item[0])
    st_men_all.append(item[2])
    if " " in item[2]:
        st_men_multi.append(item[2])
    else:
        senList_nomulti.append(item[3].replace("\n"," ").replace(item[2],"@@@@@@@@"))
    # if item[2] not in item[3]:
    #     print(item[0], item[2], item[3])
    senList.append(item[3].replace("\n"," ").replace(item[2],"@@@@@@@@"))
    articleDict.setdefault(item[0].lstrip("bioj:a"), []).append(item[2])
csvFile.close()

print(len(senList_nomulti))

with open("/home/riley/Documents/Github/Dissertation-2019/Prodigy/fileMerged_multiwords.txt", 'w', encoding="utf8") as f:
    for sen in senList_nomulti:
        slice = []
        slice = random.sample(st_men_multi, 3)
        # print(slice)
        for w in slice:
            f.write(sen.replace("@@@@@@@@",w))
            f.write("\n")


# print("Howison length", len(set(articleList)))

# print(len(st_men_all))
st_men_all = sorted(set(st_men_all))
# print(len(st_men_all))

# print(st_men_all)

st_men_all_new = [w for w in st_men_all if " " not in w ]
# print(st_men_all_new)
# print(len(st_men_all_new))


n = 0
folder_out = os.getcwd() + "/testdata"
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
txtFiles_nosupple = [f for f in txtFiles if "Supplemen" not in f]
# print("Text length", len(set(txtFiles_nosupple)))
os.chdir(folder_out)
for key, value in articleDict.items():
    for txtFile in txtFiles_nosupple:
        flag = True
        if key in txtFile.strip(".txt"):
            document = open(txtFile, "r", encoding='utf-8').read()
            for v in value:
                if v.lower() not in document.lower():
                    n += 1
                    flag = False
                    # print(v)
            # print(txtFile, flag)
# print(n)



