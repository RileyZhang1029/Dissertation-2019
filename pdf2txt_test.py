import os
import re
import string
from tika import parser


def convert_pdf_to_txt(path):
    try:
        raw = parser.from_file(path)
        text = raw['content']

        printable = set(string.printable)
        for ch in text:
            if ch not in printable:
                text_fil = text.replace(ch, '')

        textClearLink = re.sub(r"[\n](http://[^ ]+)[\n]", '', text_fil)
        textNoSpace = textClearLink.replace('\n\n', '\n').replace('\n', ' ').replace('  ', ' ').replace(' -', '-').replace('- ', '-').replace('// ', '//').replace('www. ', 'www.').replace('Fig. ', 'Fig.')
        case = [' /', ' / ']
        for c in case:
            if c in textNoSpace:
                textNoSpace = textNoSpace.replace(c, '/')

        with open(path[:-3] + 'txt', "w", encoding='utf-8') as f:
                f.write(textNoSpace.strip())

    except Exception as e:
        print("ERROR：" + path)
        # if os.path.exists(path):
        #     os.remove(os.path.join(path))
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
    rootdir = os.getcwd() + "/testdata"
    traversal(rootdir)










