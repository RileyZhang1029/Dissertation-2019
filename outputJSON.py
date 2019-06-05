# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:16:00 2019

@author: Administrator
"""
import os 
import json
import spacy
nlp = spacy.load('en')  

folder_out = os.getcwd() + "\\test"

files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
print(len(txtFiles))
os.chdir(folder_out)
with open("doc.json", 'w', encoding = "utf8") as f:
    for txtFile in txtFiles:
        #遍历单个文件，读取行数 
        try:
            for line in open(txtFile, encoding = 'utf8'):
                dic_doc = {}
                dic_doc["text"]=line.replace('\n','')
#                f.writelines(line.replace('\n',''))
                doc = nlp(line)
                list_doc = []
                for ent in doc.ents:
                    list_doc.append([ent.start_char, ent.end_char, ent.label_])
                dic_doc["labels"]=list_doc
                if (dic_doc != {'text': '', 'labels': []} and dic_doc['labels'] != []):
                    json.dump(dic_doc,f)
                    f.write('\n')
                    print(dic_doc)
        except UnicodeDecodeError:
            print("error:" + txtFile)
            pass
                
  



