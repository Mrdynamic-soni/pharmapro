# libraries to complete the task
import openpyxl
from bs4 import BeautifulSoup
import html5lib
import os

file_path = "C:\\Users\\Acer\\Desktop\\PHARMAPRO" #path of folder
os.chdir(file_path) #changing path to folder
# path of the excel file
path = "C:\\Users\\Acer\\Desktop\\PHARMAPRO\\Data.xlsx"
row_count = 2  #iterator for row
#opening all html files from folder 
for file in os.listdir():
    if file.endswith(".html"):
        #open excel file using openpyxl library
        wb_obj = openpyxl.load_workbook(path)
        sheet_obj = wb_obj.active # storing all the active shells from excel
        # path of webpage
        myFile=open(file,'r',encoding="utf8")
        #creating soup to 
        soup=BeautifulSoup(myFile,"html5lib")
        tb = soup.find_all('table')
        # print(tb)
        i=1
        for j in soup.find_all('tr')[1:]:   
            row_data = j.find_all('td')
            row = [tr.text for tr in row_data]
            if len(row)==1:
                continue
            sheet_obj.cell(row=row_count,column=i).value = row[1]
            wb_obj.save(path)
            i+=1
        row_count+=1





        # print(row[1])
        # length = len(df)
