import os
import re
import string
from tika import parser
from nltk.tokenize import sent_tokenize


def convert_pdf_to_txt(path):
    try:
        raw = parser.from_file(path)
        text = raw['content']
        text_fil = text.replace("-\n", "--").replace("--\n", "")





        with open(path[:-3] + 'txt', "w", encoding='utf-8') as f:

                f.write(text_fil)
                f.write('\n')

    except Exception as e:
        print("ERROR：" + path)
        if os.path.exists(path):
            os.remove(os.path.join(path))
        if os.path.exists(path.replace("pdf", "txt")):
            os.remove(os.path.join(path.replace("pdf", "txt")))
        pass


def traversal(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            filenamefull = os.path.join(parent, filename)
            if filenamefull.endswith('pdf') or filenamefull.endswith('PDF'):
                convert_pdf_to_txt(filenamefull)



if __name__ == '__main__':
    rootdir = os.getcwd() + "/ttt"
    traversal(rootdir)










