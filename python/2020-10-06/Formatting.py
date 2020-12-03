year = 2020
month = 10
day = 6

a = '%d-%02d-%02d' % (year, month, day)
print(a)

name = '김두한'
b = '나는 %s입니다.' % name
print(b)

age = 20
c = '나이는 %d살 입니다.' % age
print(c)

height = 172.5
d = '키는 %.2f입니다.' % height
print(d)

eyesight = 1.2

x = '이름 : {}'.format(name)
y = '나이 : {}세'.format(age)
z = '시력 : {}'.format(eyesight)

print(x)
print(y)
print(z)