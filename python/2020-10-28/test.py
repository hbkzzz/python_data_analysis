temper = [
    ['2020-10-01', 15.7, 27.4, 11.7],
    ['2020-10-02', 16.3, 28.3, 12.0],
    ['2020-10-03', 14.2, 27.6, 13.0],
    ['2020-10-04', 17.9, 25.8, 7.9],
    ['2020-10-05', 18.2, 23.8, 5.6],
    ['2020-10-06', 17.3, 25.8, 8.5],
    ['2020-10-07', 12.9, 23.8, 10.9],
    ['2020-10-08', 11.9, 25.6, 13.7],
    ['2020-10-09', 14.5, 27.3, 12.8],
    ['2020-10-10', 15.3, 26.8, 11.5]
]

for i in range(len(temper)) :
    temper_date = ''
    temper_sum = 0
    temper_avg = 0

    for j in range(len(temper[i])) :
        if (j == 0) :
            temper_date = temper[i][0]
        else :
            temper_sum = temper_sum + temper[i][j]
    
    temper_avg = temper_sum / (len(temper[i]) - 1)
    temper_date = temper_date[0:4] + '년 ' + \
        temper_date[5:7] + '월 ' + \
        temper_date[8:] + '일'

    print('%s의 온도총합 : %d도, 평균온도 : %d도' % (temper_date, temper_sum, temper_avg))


