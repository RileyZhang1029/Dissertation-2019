import sys
import importlib
importlib.reload(sys)
import codecs

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import spacy
nlp = spacy.load('en')                       # load model with shortcut link "en"
#nlp = spacy.load('en_core_web_sm')           # load model package "en_core_web_sm"
#nlp = spacy.load('/path/to/en_core_web_sm')  # load package from a directory

'''
 Read a pdf file and save it into a txt file.
'''
path = r'journal1.pdf'
def parse():
    fp = open(path, 'rb') 
    praser = PDFParser(fp)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)

    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages(): 
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open('journal2.txt', 'a', encoding='utf-8') as f:
                        results = x.get_text()
#                        print(results)
                        f.write(results + '\n')

#posTag
def posTag(doc):                        
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)
        
        
#NER
def NER(doc):          
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)        


if __name__ == '__main__':
    
    parse()
    document = codecs.open('journal1.txt', encoding='utf-8', errors='replace').read()
    doc = nlp(document)
    print(len(document))
    posTag(doc)
    NER(doc)
