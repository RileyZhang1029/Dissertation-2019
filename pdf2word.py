
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
import os
 
def pdf_to_txt(folder_out, password):
    # 获取指定目录下面的所有文件
    files = os.listdir(folder_out)
    # 获取pdf类型的文件放到一个列表里面
    pdfFiles = [f for f in files if f.endswith(".pdf")]
    for pdfFile in pdfFiles:
        # 将pdf文件放到指定的路径下面
        pdfPath = os.path.join(folder_out, pdfFile)
        # 设置将要转换后存放word文件的路径       
        wdPath = pdfPath
        
        # 判断是否已经存在对应的word文件，如果不存在就加入到存放word的路径内
        if wdPath[-3:] != 'txt':
            wdPath = wdPath + ".txt"
            fn = open(pdfPath, 'rb')
            # 创建一个PDF文档分析器：PDFParser
            parser = PDFParser(fn)
            # 创建一个PDF文档：PDFDocument
            doc = PDFDocument()
            # 连接分析器与文档
            parser.set_document(doc)
            doc.set_parser(parser)
            # 提供初始化密码，如果无密码，输入空字符串
            doc.initialize("")
            # 检测文档是否提供txt转换，不提供就忽略
            if not doc.is_extractable:
                print("PDFTextExtractionNotAllowed")
            else:
                # 创建PDF资源管理器：PDFResourceManager
                resource = PDFResourceManager()
                # 创建一个PDF参数分析器：LAParams
                laparams = LAParams()
                # 创建聚合器,用于读取文档的对象：PDFPageAggregator
                device = PDFPageAggregator(resource, laparams=laparams)
                # 创建解释器，对文档编码，解释成Python能够识别的格式：PDFPageInterpreter
                interpreter = PDFPageInterpreter(resource, device)
                # doc.get_pages() 获取page列表
                for page in doc.get_pages():
                    # 利用解释器的process_page()方法解析读取单独页数
                    interpreter.process_page(page)
                    # 这里layout是一个LTPage对象,里面存放着这个page解析出的各种对象,
                    # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal等等,想要获取文本就获得对象的text属性，
                    # 使用聚合器get_result()方法获取页面内容
                    layout = device.get_result()
                    for out in layout:
                        if (isinstance(out, LTTextBoxHorizontal)):
                            print(out.get_text())
                            with open(wdPath, 'a',encoding='utf-8') as f:
                                f.write(out.get_text() + '\n')
                            

if __name__ == '__main__':
    
    pdf_to_txt("E:/ed/Dissertation/Howisonproject/softcite-master/data/pdf_articles/text_error","")
    
