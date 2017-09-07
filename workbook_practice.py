from xlsxwriter import Workbook

wb_name = str(input("Enter Name of  Workbook: "))

if '.xlsx' not in wb_name:
    wb_name += '.xlsx'

wb = Workbook('workbook_output/' + wb_name)
ws = wb.add_worksheet(input("Enter Worksheet name: "))
for i in range(51):
    for j in range(51):
        data = '%d, %d' % (i,j)
        ws.write(i, j, data)
wb.close()