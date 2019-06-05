# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:03:35 2019

@author: Administrator
"""
#need uninstall pdfminer3k and install pdfminer.six

# encoding: utf-8
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os 
from nltk.tokenize import sent_tokenize
import re


def convert_pdf_to_txt(path, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
      
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(path, 'rb')
#    try:
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    for ch in text:
        if not ch.isalnum() and ch not in "[.-\/()+$%^&*=,@#:_!']":
            text = text.replace(ch,' ')
            
    with open(path[:-3]+'txt', "w", encoding='utf-8') as f:
        sentences = sent_tokenize(text)
        for s in sentences:
            f.write(s.replace('\n',' ').strip())
            f.write('\n')
        
#    except Exception as e:
#        print("ERROR：" + path)
#        pass

        

def traversal(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            filenameFull = os.path.join(parent, filename)
            if (filenameFull.endswith('pdf') or filenameFull.endswith('PDF')):
                convert_pdf_to_txt(filenameFull)
                # 原因是这里，把方块替换成''了，应该替换成空格。

if __name__=='__main__':
    rootdir = os.getcwd() +"\\test"
    traversal(rootdir)
        
        
        
        
        