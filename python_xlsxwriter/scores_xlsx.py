import xlsxwriter

workbook = xlsxwriter.Workbook('./data/excel/scores.xlsx')
worksheet = workbook.add_worksheet()

scores = (
    ['안녕', 88],
    ['구름', 75],
    ['서울', 90],
    ['강', 95],
    ['바람', 77],
    ['하늘', 69],
    ['시원', 80],
    ['가을', 92],
)
row = 0
col = 0

for name, score in scores :
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, score)
    row += 1

worksheet.write(row, 0, '총합')
worksheet.write(row, 1, '=SUM(B1:B8)')
worksheet.write((row + 1), 0, '평균')
worksheet.write((row + 1), 1, '=AVERAGE(B1:B8)')
worksheet.write((row + 2), 0, '최대점수')
worksheet.write((row + 2), 1, '=MAX(B1:B8)')
worksheet.write((row + 3), 0, '최소점수')
worksheet.write((row + 3), 1, '=MIN(B1:B8)')

workbook.close()