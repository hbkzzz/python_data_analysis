'''
for x in range(5) :
    print('안녕하세요.')
'''

# 1~10의 합계
sum = 0
fromValue = 1    # for 루프 시작값
toValue = 11     # for 루프 끝

for i in range(fromValue, toValue) :
    sum += i
    print('i의 값 : %d, 합계 : %d' % (i, sum))