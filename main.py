# import sys
# import urllib.request

# original_stdout = sys.stdout

from bs4 import BeautifulSoup
import html5lib
myFile=open("C:\\Users\\Acer\\Desktop\\PHARMAPRO\\59978.html",'r',encoding="utf8")
soup=BeautifulSoup(myFile,"html5lib")
# print(soup.title.text1
# print(soup.text)
# for i in soup.table.td.tr.b.text:
for i in soup.find_all(soup.table.td.tr.b):
    print(i)
# print(soup.table.td.tr.b.text)