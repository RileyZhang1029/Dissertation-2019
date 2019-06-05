# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:48:37 2019

@author: Administrator
"""
import os
import spacy
nlp = spacy.load('en')                       # load model with shortcut link "en"(just change here after training a new category)


        
#命名实体识别
def NER(doc):          
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)        


if __name__ == '__main__':
#    parse()
#    posTag(doc)
#    NER(doc)
    
    folder_out = os.getcwd() + "\\trainingdata1"
    files = os.listdir(folder_out)
    txtFiles = [f for f in files if f.endswith(".txt")]
    print(len(txtFiles))
    
#    with open("C:/Users/Administrator/Documents/GitHub/Dissertation-2019/pdf_articles/docCleaned.txt", 'w', encoding = "utf8") as f:
    for txtFile in txtFiles:    
        os.chdir(folder_out)
#    document = unicode(open(filename).read().decode('utf8'))
        document = open(txtFile, "r", encoding='utf-8').read()
        doc = nlp(document)
        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)
        









