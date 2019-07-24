import os
import re
import string
from tika import parser
from nltk.tokenize import sent_tokenize
import numpy as np
import xlrd  # 打开excel文件


def convert_pdf_to_txt(path):
    try:
        raw = parser.from_file(path)
        text_fil = raw['content']
        text_fil = text_fil.replace("-\n", "")
        printable = set(string.printable)
        for ch in text_fil:
            if ch not in printable:
                text_fil = text_fil.replace(ch, '')

        textClearLink = re.sub(r"[\n](http://[^ ]+)[\n]", '', text_fil)
        textClearLink = ' '.join(textClearLink.split())
        textNoSpace = textClearLink.replace('\n\n', '\n').replace('\n', ' ').replace(' .', '.').replace(' ,', ',').replace(' -', '-').replace('- ', '-').replace('// ', '//').replace('www. ', 'www.').replace('Fig. ', 'Fig.').replace('e.g.\n', 'e.g.').replace(' .', '.')
        case = [' /', ' / ']
        for c in case:
            if c in textNoSpace:
                textNoSpace = textNoSpace.replace(c, '/')

        sentences = sent_tokenize(textNoSpace)
        with open(path[:-3] + 'txt', "w", encoding='utf-8') as f:
            for s in sentences:
                f.write(s)
                if s.endswith('e.g.') or s.endswith('i.e.') or s.endswith('et al.'):
                    f.write('')
                else:
                    f.write('\n')
        # with open(path[:-3] + 'txt', "w", encoding='utf-8') as f:
        #     f.write(textNoSpace)
        #     f.write('\n')
    except Exception as e:
        print("ERROR：" + path)
        # if os.path.exists(path):
        #     os.remove(os.path.join(path))
        # if os.path.exists(path.replace("pdf", "txt")):
        #     os.remove(os.path.join(path.replace("pdf", "txt")))
        pass






def convert_xls_to_txt(path):
    data = xlrd.open_workbook(path)  # 打开Excel文件读取数据
    sheetnames = data.sheet_names()
    with open(path[:-3] + 'txt', "w", encoding='utf-8') as f:
        for name in sheetnames:
            sh = data.sheet_by_name(name)  ##通过工作簿名称获取
            for n in range(sh.nrows):
                for i in range(sh.ncols):
                    text = sh.cell_value(n, i)
                    f.write(str(text))
                    f.write('\n')



def traversal(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            filenamefull = os.path.join(parent, filename)
            if filenamefull.lower().endswith('pdf'):
                convert_pdf_to_txt(filenamefull)
            if filenamefull.lower().endswith('xls'):
                print(filenamefull)
                convert_xls_to_txt(filenamefull)
            # if filenamefull.lower().endswith('doc'):
            #     convert_doc_to_txt(filenamefull)




if __name__ == '__main__':
    rootdir = os.getcwd() + "/testdata"
    traversal(rootdir)










