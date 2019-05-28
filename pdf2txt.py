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


def readPDF(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text



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
    try:
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close()
        with open(path[:-3]+'txt', "w", encoding='utf-8') as f:
            print('openTxt:' + path[:-3]+'txt')
            f.write(text.replace(u'\xa9', u'').replace(u'\xa0',u'').replace(u'\xad',u'').replace(u'\u037e',u''))
    except Exception as e:
        print("ERROR：" + path)
        pass

def traversal(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            filenameFull = os.path.join(parent, filename)
            if (filenameFull.endswith('pdf') or filenameFull.endswith('PDF')):
#                txt = readPDF(filenameFull)
                convert_pdf_to_txt(filenameFull)
                # 原因是这里，把方块替换成''了，应该替换成空格。

if __name__=='__main__':
    rootdir = "C:/Users/Administrator/Documents/GitHub/Dissertation-2019/pdf_articles/pdf2txt"
    traversal(rootdir)