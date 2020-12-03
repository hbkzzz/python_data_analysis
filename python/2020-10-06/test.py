# Q1
'''
a = 7
b = 10

c = a + b * 2
c %= 5
c **= 3
c -= c * 10

print(c) # 실행 결과 -72
'''

# Q2
'''
r = int(input("반지름을 입력하세요 : "))
pi = 3.14
won = float(2 * pi * r)
won2 = float(pi * (r ** 2))
print("반지름 : %d" % r + "cm")
print("원의 둘레 : %.2f " % won + "cm")
print("원의 면적 : %.2f " % won2 + "cm2")
'''

# Q3
'''
book = int(input("책 값을 입력하세요 : "))
discount = int(input("할인율을 입력하세요(%) : "))
shipping = int(input("배송료를 입력하세요 : "))
price = book - int(book * discount / 100) + shipping
a = '결제 금액 : {}원'.format(price)
print(a)
'''

# Q4
'''
name = input("이름을 입력하세요 : ")
year = int(input("현재년을 입력하세요 : "))
birthyear = int(input("탄생년을 입력하세요 : "))
age = year - birthyear + 1
x = '{}님의 나이는 {}세 입니다!'.format(name, age)
print(x)
'''

# Q5
year = input("연을 입력하세요 : ")
month = int(input("월을 입력하세요 : "))
day = int(input("일을 입력하세요 : "))
a = "%02d" % month
b = "%02d" % day
print(year, a, b, sep='-')