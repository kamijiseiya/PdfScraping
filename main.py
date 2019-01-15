import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール

# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox
import pdf as pt
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from glob import glob


# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
##ファイルの拡張子の設定
## fTyp = [("","*")]
fTyp = [("","*.pdf")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('○×プログラム','処理ファイルを選択してください！')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
ret = pt.gettext(file)
print(ret)
