# Q1
'''
a = ('*' * 5)
for x in a :
    print(x * 10) 
'''

# Q2
'''
x = 0
while x < 5 :
    print('*' * 10)
    x += 1
'''

# Q3
'''
for a in range(6, 0, -1) :
    b = str(a)
    print(b*a)
'''

# Q4
'''
for a in range(0, 7) :
    for b in range(0, a) :
        print(b, end='')
    print()
'''

# Q5
'''
x = '*' * 8
print(x)
a = '*      *'
for b in range(6) :
    print(a)
print(x)
'''

# Q6 1~100까지의 수 중에서 홀수와 홀수의 합 출력
'''
sum = 0
for x in range(1, 101) :
    if x % 2 != 0 :
        sum = sum + x
    if x != 99 :
        print(x, end=' + ')
print('99', '=', sum)
'''

# Q7 N값을 입력 받아 2**1 + 4**3 + 6**5 + ... 2N**(2N-1) 수식의 결과를 출력
'''
n = int(input('N의 값을 입력하세요 : '))
sum = 0

for i in range(1, n+1) :
    a = (2 * i) ** (2 * i - 1)
    sum += a

print('N의 값 : %d' % n)
print('합계 : %d' % sum)
'''

# Q8 N값을 입력받아 1부터 N까지의 수 중에서 소수를 구하시오.
# 소수 : 1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의 정수.
'''
n = int(input('N 값을 입력해 주세요 : '))

for i in range(1, n+1) :
    a = True
    if i == 1 : 
        a = False
    for j in range(2, i) :
        if i % j == 0 :
            a = False
            break
    if a :
        print(i, end=' ')
'''

# Q9 while 문을 이용하여 달러(＄), 원화(￦), 유로(€)의 환산표를 만드시오
# 1달러 당 환율 : 1080(원화), 0.81(유로)
'''
a = '-' * 50
x = 10

print(a)
print('달러(＄)', '원화(￦)', '유로(€)')
print(a)

while x < 101 :
    b = x * 1080
    c = x * 0.81
    print('  %d     %d    %.1f' % (x, b, c))
    x += 10

print(a)
'''

# Q10 while 문을 이용하여 센티미터(cm), 밀리미터(mm), 미터(m), 인치(inch)의 길의 환산표를 만드시오

a = '-' * 50
x = 1

print(a)
print('    cm    ', 'mm    ', 'm    ', 'inch')
print(a)

while x < 100 :
    b = x * 10
    c = x * 0.01
    d = x * 0.3937
    print('   %d     %d    %.2f    %.2f' % (x, b, c, d))
    x += 2

print(a)