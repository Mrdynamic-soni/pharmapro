import webbrowser
import openpyxl

path = "C:\\Users\\Acer\\Desktop\\PHARMAPRO\\Data.xlsx"

wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

# cell = sheet_obj.cell(row=1,column = 1)
# print(cell.value)

for i in range(1,sheet_obj.max_column+1):
    print(sheet_obj.cell(row=1,column=i).value)