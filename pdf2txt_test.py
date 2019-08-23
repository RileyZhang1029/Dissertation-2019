"""
B134977
Convert PDF files in test data into Texts (do not remove contents before abstract)
link to the Github Repostory: https://github.com/RileyZhang1029/Dissertation-2019
"""

import os
import string
from tika import parser
from nltk.tokenize import sent_tokenize
import xlrd


def convert_pdf_to_txt(path):
    try:
        raw = parser.from_file(path)
        text = raw['content']
        text = text.replace("-\n", "")
        if "2007-11-GENOME_RES.pdf" in path or "2001-16-CELL.pdf" in path or "2001-50-CELL.pdf" in path or "2004-46-NATURE" in path or "2004-44-DEV_CELL" in path or "2009-35-CELL" in path:
            text_fil = text
        else:
            if text.lower().find('references\n'):
                text_fil = text[:text.lower().find('references\n')]
            else:
                print("error: ", path)

        printable = set(string.printable)
        for ch in text_fil:
            if ch not in printable:
                text_fil = text_fil.replace(ch, '')


        textNoSpace = text_fil.replace('\n\n', '\n').replace('\n', ' ').replace('  ', ' ')
        case = [' /', '/ ', ' -', '- ', '// ', 'www. ', 'Fig. ', ' .']
        for c in case:
            if c in textNoSpace:
                textNoSpace = textNoSpace.replace(c, c.strip(' '))

        sentences = sent_tokenize(textNoSpace)
        with open(path[:-3] + 'txt', "w", encoding='utf-8') as f:
            for s in sentences:
                f.write(s.strip(' '))
                if s.endswith('e.g.') or s.endswith('i.e.') or s.endswith('et al.'):
                    f.write('')
                else:
                    f.write('\n')

    except Exception as e:
        print("ERROR：" + path)
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

if __name__ == '__main__':
    rootdir = os.getcwd() + "/testdata"
    traversal(rootdir)










