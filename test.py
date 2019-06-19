# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:03:35 2019

@author: Administrator
"""
# need uninstall pdfminer3k and install pdfminer.six

# encoding: utf-8

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
from nltk.tokenize import sent_tokenize
import re
import enchant


def word_check(s):
    list_s = s.strip('.').strip('/').split()
    lastword = list_s[-1].lower()
    list_con = ["vol", "no", "fig"]
    flag = True
    for con in list_con:
        if lastword == con:
            flag = False
            print(s)
            break
        else:
            try:
                usCHECK = enchant.Dict("en_US")
                flag = usCHECK.check(lastword)
            except ValueError:
                print("ERROR：" + s)
                pass
    return flag


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
        # for ch in text:
        #     if not ch.isalnum() and ch not in "[.-\/()+$%^&*=,@#:_!']":
        #         text = text.replace(ch, ' ')
        # text = text[:(text.find('REFERENCES'))]
        # print(text)

        with open(path[:-3] + 'txt', "w", encoding='utf-8') as f:
            f.write(text)
            # sentences = sent_tokenize(text)
            # for s in sentences:
            #     s = s.replace('  ', ' ').replace(' .', '.').strip()
            #     list_s = s.strip('.').strip('/').split()
            #     lastword = list_s[-1].lower()
            #     usCHECK = enchant.Dict("en_US")
            #     list_con = ["vol", "no", "fig", "sci", "j", "am", "stat"]
            #     # flag = True
            #     s = s.replace("/ ", " ").replace(" -", "-").replace("- ", "-").replace(" ,", ",").replace(" .", ".")
            #     if lastword in list_con:
            #         f.write(s)
            #     else:
            #         try:
            #             if usCHECK.check(lastword):
            #                 f.write(s + '\n')
            #             else:
            #                 f.write(s + ' ')
            #         except ValueError:
            #             print("ERROR：" + s)
            #             f.write(s + '\n')
            #             pass
    #
    except Exception as e:
        print("ERROR：" + path)
        # os.remove(os.path.join(path))
        # os.remove(os.path.join(path.replace("pdf", "txt")))
        pass


def traversal(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            filenamefull = os.path.join(parent, filename)
            if filenamefull.endswith('pdf') or filenamefull.endswith('PDF'):
                convert_pdf_to_txt(filenamefull)


if __name__ == '__main__':
    rootdir = os.getcwd() + "/test"
    traversal(rootdir)


