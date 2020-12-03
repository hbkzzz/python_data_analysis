def min(a, b) :
    if (a <= b) :
        return a
    else :
        return b

def max(a, b) :
    if (a >= b) :
        return a
    else :
        return b

# main()
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
temper_min_min = 100
temper_min_max = 0
temper_max_min = 100
temper_max_max = 0
temper_diff_min = 100
temper_diff_max = 0

for i in range(list_count) :
    for j in range(len(temper[i])) :
        if (j == 0) :
            temper_date = temper[i][0]
        elif (j == 1) :
            temper_min_min = min(temper_min_min, temper[i][j])
            temper_min_max = max(temper_min_max, temper[i][j])
        elif (j == 2) :
            temper_max_min = min(temper_max_min, temper[i][j])
            temper_max_max = max(temper_max_max, temper[i][j])
        elif (j == 3) :
            temper_diff_min = min(temper_diff_min, temper[i][j])
            temper_diff_max = max(temper_diff_max, temper[i][j])


temper_date = temper_date[0:4] + "년 " + temper_date[5:7] + "월"

print("\'%s\' 중 \n최저기온 중 최저기온 : \'%.1f\'도, 최고기온 : \'%.1f\'도 \
\n최고기온 중 최저기온 : \'%.1f\'도, 최고온도 : \'%.1f\'도 \
\n일교차 \t 중 최저기온 : \'%.1f\'도, 최고온도 : \'%.1f\'도" % \
(temper_date, temper_min_min, temper_min_max, temper_max_min, temper_max_max, temper_diff_min, temper_diff_max))