# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:48:37 2019

@author: Administrator
"""
import spacy
from spacy import displacy
from collections import Counter
from pprint import pprint
import sys
import importlib
importlib.reload(sys)
import codecs


nlp = spacy.load('en')                       # load model with shortcut link "en"
#nlp = spacy.load('en_core_web_sm')           # load model package "en_core_web_sm"
#nlp = spacy.load('/path/to/en_core_web_sm')  # load package from a directory

#词性标注
def posTag(doc):                        
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        
        
#命名实体识别
def NER(doc):          
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)        


if __name__ == '__main__':
#    parse()
#    document = codecs.open('journal1.txt', encoding='utf-8', errors='replace').read()
#    doc = nlp(document)
#    print(len(document))
#    posTag(doc)
#    NER(doc)



#doc2 = nlp('We will use NER to realize this hypothesis, taking spaCy as the library and Prodigy as the tool.')
#pprint([(X.text, X.label_) for X in doc2.ents])
