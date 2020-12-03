import xlsxwriter

workbook = xlsxwriter.Workbook('./data/excel/hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello')
worksheet.write('B1', 'World')

worksheet.write(0, 2, "It's me")

worksheet.write(1, 0, 2)
worksheet.write(1, 1, 4)
worksheet.write(2, 0, '= A2 + B2')

workbook.close()