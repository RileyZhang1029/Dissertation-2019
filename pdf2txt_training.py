"""
B134977
Convert PDF files in training data into Texts (remove contents before abstract)
link to the Github Repostory: https://github.com/RileyZhang1029/Dissertation-2019
"""

import os
import string
from tika import parser
from nltk.tokenize import sent_tokenize


def convert_pdf_to_txt(path):
    try:
        raw = parser.from_file(path)
        text = raw['content']
        text = text.replace("-\n", "--").replace("--\n", "").replace("--","")
        if text.lower().find('references\n'):
            text_fil = text[:text.lower().find('references\n')]
        else:
            print("error: ", path)
            if os.path.exists(path):
                os.remove(os.path.join(path))
            if os.path.exists(path.replace("pdf", "txt")):
                os.remove(os.path.join(path.replace("pdf", "txt")))
        if text.lower().find('abstract\n'):
            text_fil = text_fil[text_fil.lower().find('abstract\n')+9:]
        else:
            print("error: ", path)
            # if os.path.exists(path):
            #     os.remove(os.path.join(path))
            # if os.path.exists(path.replace("pdf", "txt")):
            #     os.remove(os.path.join(path.replace("pdf", "txt")))

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
    rootdir = os.getcwd() + "/trainingdata"
    traversal(rootdir)










