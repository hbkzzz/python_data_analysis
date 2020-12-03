# 입력받은 숫자 중 홀수 갯수 구하기
num = input('숫자를 입력하세요 : ')

total = 0

for a in num :
    a = int(a)
    if a % 2 == 1 :
        total += 1

print('입력된 숫자 중 홀수의 개수 : %d개' % total)