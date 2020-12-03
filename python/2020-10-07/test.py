# Q1
'''
a = 2
z = a * 5
w = (z - 3) * (a - 2) / 7 + 10

if a > z or w > a :
    y = 2 * a
else :
    y = 4 * a

print(y) # 실행 결과 = 4
'''

# Q2
'''
a = input('단위를 입력하세요(1:섭씨, 2:화씨): ')
f = int(input('온도를 입력하세요: '))
x = f
state = '기체'

if a != '1' :
    x = float((f - 32) * 5 / 9)

if x <= 0 :
    state = '고체'
elif x >= 1 and x <= 99 :
    state = '액체'

print('물의 섭씨 온도 : %.2f, 상태 : %s' % (x, state))
'''

# Q3
'''
name = input('아이디를 입력하세요 : ')
level = int(input('회원 레벨을 입력해 주세요 : '))
x = ''

if name == 'admin' :
    x = '모든 콘텐츠 이용 가능'
elif level >= 2 and level <=7 :
    x = '일부 콘텐츠 이용 가능' 
else :
    x = '콘텐츠 이용 불가'

print(x)
'''

# Q4
'''
age = int(input('나이를 입력하세요 : '))
price = 2000

if age <= 10 :
    price = 1000
elif age >= 65 :
    price = 0

print('입장료는 %d원 입니다' % price)
'''

# Q5

eng = int(input('영어시험 점수를 입력하세요 : '))
math = int(input('수학시험 점수를 입력하세요 : '))
x = '불합격'

if eng >= 80 and math >= 80 :
    x = '합격'
elif eng >= 80 or math >= 80 :
    x = '재시험 기회제공'

print(x)