# libraries to complete the task
import openpyxl
from bs4 import BeautifulSoup
import html5lib


# path of the excel file
path = "C:\\Users\\Acer\\Desktop\\PHARMAPRO\\Data.xlsx"
#open excel file using openpyxl library
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active # storing all the active shells from excel
# path of webpage
myFile=open("C:\\Users\\Acer\\Desktop\\PHARMAPRO\\59978.html",'r',encoding="utf8")
#creating soup to 
soup=BeautifulSoup(myFile,"html5lib")
tb = soup.find_all('table')


# print(tb)
i=1
for j in soup.find_all('tr')[1:]:   
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        if row[0]== 'FULL DETAILS (Read-only) \xa0->\xa0Click Here to Create PDF for Current Dataset of Trial':
            continue
        sheet_obj.cell(row=2,column=i).value = row[1]
        wb_obj.save(path)
        i+=1
        # print(row[1])
        # length = len(df)
