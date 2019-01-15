import os
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

pdf_folder_path = os.getcwd()
text_folder_path = os.getcwd() + '/' 

print(text_folder_path)
