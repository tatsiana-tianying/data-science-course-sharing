import openpyxl
wb = openpyxl.load_workbook("writing_in_xl.xlsx")
sheet = wb.active
c = sheet['A3']
c.value = "New Data"
wb.save("writing_in_xl.xlsx")
