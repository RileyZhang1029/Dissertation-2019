# -*- coding: utf-8 -*-
"""
B134977
This file will load the spaCy NER model and perform test on the test set (texts in the directory /path/to/testdata/)
It will load a CSV file that contains Howison's results, read the software mentions.
The it will output 'NER_results.txt' which contains the comparison results of each article.
link to the Github Repostory: https://github.com/RileyZhang1029/Dissertation-2019
"""

import os
import csv
import spacy


def readCSV(csvpath):
    csvFile = open(csvpath)
    reader = csv.reader(csvFile)
    articleList = []
    articleDict = {}
    st_men_all = []

    for item in reader:
        if reader.line_num == 1:
            continue
        articleList.append(item[0])
        # if " " not in item[2]:
        st_men_all.append(item[2])
        articleDict.setdefault(item[0].lstrip("bioj:a"), []).append(item[2])
    csvFile.close()

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
    print("n =", n)
    return wordlist_all

#comput precision, recall, and f-score
def PRF(list1, list2):
    list1 = [i.lower() for i in list1]
    list2 = [i.lower() for i in list2]
    tplist = [i for i in list1 if i in list2]

    print("Common software mentions: ", tplist)
    print("Number of common software mentions: ", len(tplist))
    precision = len(tplist)/len(list2)
    recall = len(tplist)/len(list1)
    fscore = 2*precision*recall/(precision+recall)

    return [precision,recall,fscore]


if __name__ == '__main__':
    csvpath = "/path/to/results_each_article.csv", "r"
    model = "/home/riley/Documents/Github/models/st-model-all-nn-it30dp20bt16"
    #directory of test set
    folder_out = os.getcwd() + "/testdata"
    word_list_sorted = NER(model, folder_out)
    print(word_list_sorted)

    #list of all software mentions in Howison et sl.'s results
    st_men_all = readCSV()[1]
    print(st_men_all)

    PRF = PRF(st_men_all, word_list_sorted)
    precision = PRF[0]
    print("The precision of the model is: ", precision)

    recall = PRF[1]
    print("The recall of the model is: ", recall)

    fscore = PRF[2]
    print("The fscore of the model is: ", fscore)

















