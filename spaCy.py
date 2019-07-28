# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:48:37 2019

@author: Administrator
"""
import os
import spacy
import csv


def readCSV():
    csvFile = open("/home/riley/Documents/Github/Dissertation-2019/results_each_article.csv", "r")
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

    st_men_all = sorted(set(st_men_all))

    return (articleDict, st_men_all)


def NER(model, folder_out):
    nlp = spacy.load(model)
    files = os.listdir(folder_out)
    txtFiles = [f for f in files if f.endswith(".txt")]
    print("Number of the textfile is: ", len(txtFiles))
    txtFiles = sorted(txtFiles)
    txtFiles_nosupple = [f for f in txtFiles if "Supplemen" not in f]
    print(len(txtFiles_nosupple))
    wordlist_all = []
    n = 0
    articleDict = readCSV()[0]

    with open('NER_results.txt', "w", encoding='utf-8') as f:
        for txt_nosupple in txtFiles_nosupple:
            f.write(txt_nosupple.rstrip(".txt") + ":\n")
            f.write("Howison Results: ")
            if txt_nosupple.rstrip(".txt") in articleDict.keys():
                n += 1
                for word in articleDict[txt_nosupple.rstrip(".txt")]:
                    f.write(word + ", ")
            else:
                f.write("No Software Mentions, ")
            f.write("\n")
            f.write("NER Results: ")

            for txtFile in txtFiles:
                wordlist = []
                if txt_nosupple.strip(".txt") in txtFile.strip(".txt"):
                    print(txt_nosupple.strip(".txt"))
                    print(txtFile.strip(".txt"))
                    print("\n")
                    os.chdir(folder_out)
                    document = open(txtFile, "r", encoding='utf-8').read()
                    doc = nlp(document)
                    for ent in doc.ents:
                        if (ent.label_ == "SOFTWARE"):
                            wordlist.append(ent.text)
                            wordlist_all.append(ent.text)
                            # print(ent.text, ent.start_char, ent.end_char, ent.label_)
                    if wordlist != []:
                        for i in sorted(set(wordlist)):
                            f.write(i + ", ")

                    else:
                        f.write("No Software Mentions, ")
            f.write('\n\n')
    wordlist_all_sorted = sorted(set(wordlist_all))
    print("n =", n)
    return wordlist_all_sorted


def readHow():
    howlist = []
    with open('/home/riley/Documents/Github/Dissertation-2019/Howsresults.txt', "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            howlist.append(line.strip())
    return sorted(howlist)




def PRF(list1, list2):
    list1 = [i.lower() for i in list1]
    list2 = [i.lower() for i in list2]
    tplist = [i for i in list1 if i in list2]
    tplist = sorted(set(tplist))
    wrongExamples = [i for i in list2 if i not in tplist]
    with open("/home/riley/Documents/Github/Dissertation-2019/Prodigy/wrongExamples1.txt", 'w', encoding="utf8") as f:
        for w in wrongExamples:
            f.write(w.lower())
            f.write("\n")


    print("Common software mentions: ", tplist)
    print("Number of common software mentions: ", len(tplist))
    precision = len(tplist)/len(list2)
    recall = len(tplist)/len(list1)
    fscore = 2*precision*recall/(precision+recall)

    return [precision,recall,fscore]


if __name__ == '__main__':

    model = '/home/riley/Documents/Github/models/st-model-all'
    folder_out = os.getcwd() + "/testdata"
    word_list_sorted = NER(model, folder_out)
    print(word_list_sorted)

    # howlist = readHow()
    # print(howlist)

    st_men_all = readCSV()[1]
    print(st_men_all)

    PRF = PRF(st_men_all, word_list_sorted)
    precision = PRF[0]
    print("The precision of the model is: ", precision)

    recall = PRF[1]
    print("The recall of the model is: ", recall)

    fscore = PRF[2]
    print("The fscore of the model is: ", fscore)

















