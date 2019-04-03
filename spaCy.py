# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:48:37 2019

@author: Administrator
"""
import spacy
from spacy import displacy
from collections import Counter
from pprint import pprint
import en_core_web_sm
nlp = en_core_web_sm.load()

doc1 = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc1.ents])

doc2 = nlp('We will use NER to realize this hypothesis, taking spaCy as the library and Prodigy as the tool.')
pprint([(X.text, X.label_) for X in doc2.ents])
