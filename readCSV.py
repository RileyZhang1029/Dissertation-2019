# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:48:37 2019

@author: Administrator
"""
import os
import spacy
import csv


def readHow():
    howlist = []
    with open('/home/riley/Documents/Github/Dissertation-2019/Howsresults.txt', "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            howlist.append(line.strip())
    return sorted(howlist)



def NER(folder_out):
    files = os.listdir(folder_out)
    txtFiles = [f for f in files if f.endswith(".txt")]
    howlist = readHow()
    wordlist = []
    with open('cor_results.txt', "w", encoding='utf-8') as f:
        for txtFile in txtFiles:
            os.chdir(folder_out)
            document = open(txtFile, "r", encoding='utf-8').read()
            for word in howlist:
                if document.find(word) != -1:
                    wordlist.append(word)
                    f.write(word + ": " + txtFile + "\n")
    print(len(set(wordlist)))

if __name__ == '__main__':

    folder_out = os.getcwd() + "/test"
    NER(folder_out)


















