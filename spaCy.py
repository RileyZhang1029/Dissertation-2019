# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:48:37 2019

@author: Administrator
"""
import os
import spacy


def NER(model, folder_out):
    nlp = spacy.load(model)
    files = os.listdir(folder_out)
    txtFiles = [f for f in files if f.endswith(".txt")]
    print(len(txtFiles))
    wordlist_all = []
    n = 0
    #    with open("C:/Users/Administrator/Documents/GitHub/Dissertation-2019/pdf_articles/docCleaned.txt", 'w', encoding = "utf8") as f:
    with open('NER_results.txt', "w", encoding='utf-8') as f:
        for txtFile in txtFiles:
            wordlist = []
            try:
                os.chdir(folder_out)
                #    document = unicode(open(filename).read().decode('utf8'))
                document = open(txtFile, "r", encoding='utf-8').read()
                doc = nlp(document)
                for ent in doc.ents:
                    if (ent.label_ == "SOFTWARE"):
                        # print(ent.text)
                        n += 1
                        wordlist.append(ent.text)
                        wordlist_all.append(ent.text)

                f.write(txtFile + ":\n")
                for i in set(wordlist):
                    f.write(i + "\n")
                f.write('\n\n')
                # print(ent.text, ent.start_char, ent.end_char, ent.label_)
            except Exception as e:
                print("ERROR: ", txtFile)
                pass
    wordlist_all_sorted = sorted(set(wordlist_all))
    # print(wordlist_all_sorted)
    # print(len(wordlist_all_sorted))
    return wordlist_all_sorted


def readHow():
    howlist = []
    with open('/home/riley/Documents/fromGit/Dissertation-2019/Howsresults.txt', "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            howlist.append(line.strip())
    return sorted(howlist)


def accuracy(list1, list2):
    tplist = [i for i in list1 if i in list2]
    accuracy = len(tplist)/len(list1)
    return accuracy


if __name__ == '__main__':
    
    model = '/home/riley/Documents/Prodigy/softwares-models'
    folder_out = os.getcwd() + "/testdata"
    word_list_sorted = NER(model, folder_out)
    print(word_list_sorted)

    howlist = readHow()
    print(howlist)

    accuracy = accuracy(howlist, word_list_sorted)
    print(accuracy)












