import xlsxwriter

workbook = xlsxwriter.Workbook('./data/excel/avg.xlsx')
worksheet = workbook.add_worksheet()

student_math_score = (
    ['홍길동', 95],
    ['유관순', 75],
    ['이순신', 98],
    ['김유신', 67]
)
row = 0
col = 0

for student, score in student_math_score :
    worksheet.write(row, col, student)
    worksheet.write(row, col + 1, score)
    row += 1

bold = workbook.add_format({'bold' : True})

worksheet.write(row, 0, 'Average', bold)
worksheet.write(row, 1, '=AVERAGE(B1:B4)', bold)

workbook.close()