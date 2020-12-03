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

list_count = len(temper)
temper_date = ''
temper_min_sum = 0
temper_min_avg = 0
temper_max_sum = 0
temper_max_avg = 0
temper_diff_sum = 0
temper_diff_avg = 0

for i in range(list_count) :
    for j in range(len(temper[i])) :
        if (j == 0) :
            temper_date = temper[i][0]
        elif (j == 1) :
            temper_min_sum += temper[i][1]
        elif (j == 2) :
            temper_max_sum += temper[i][2]
        elif (j == 3) :
            temper_diff_sum += temper[i][3]
        else :
            dummy = 0

temper_min_avg = temper_min_sum / list_count
temper_max_avg = temper_max_sum / list_count
temper_diff_avg = temper_diff_sum / list_count

temper_date = temper_date[0:4] + "년 " + temper_date[5:7] + "월"

print('%s 중 \n최저기온 평균 : %02d도 \n최고기온 평균 : %02d도 \n일교차 평균 : %02d도' % (temper_date, temper_min_avg, temper_max_avg, temper_diff_avg))