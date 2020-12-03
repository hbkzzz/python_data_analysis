import csv

f = open('./data/csv/month_temp.csv', 'r', encoding='utf-8')
lines = csv.reader(f)

next(lines)

sum = 0

for line in lines :
    if(int(line[1][8:]) <= 10) :
        sum += float(line[2])

avg = sum / 10
print('10일간 평균 기온 : %.1f' % avg)

f.close()