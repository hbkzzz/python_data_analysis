animals = ['토끼', '거북이', '사자', '호랑이']

i = 0
while i < len(animals) :
    print(animals[i])
    i += 1

print()

s = [64, 89, 100, 85, 77, 68, 79, 67, 96, 87,
    87, 36, 82, 98, 84, 76, 63, 69, 53, 22]

count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

i = 0
while i < len(s) :
    if s[i] >= 90 and s[i] <= 100 :
        count_a += 1
    if s[i] >= 80 and s[i] <= 89 :
        count_b += 1
    if s[i] >= 70 and s[i] <= 79 :
        count_c += 1
    if s[i] >= 60 and s[i] <= 69 :
        count_d += 1
    if s[i] >= 0 and s[i] <= 59 :
        count_f += 1
    i += 1

print('A학점 : %d명' % count_a)
print('B학점 : %d명' % count_b)
print('C학점 : %d명' % count_c)
print('D학점 : %d명' % count_d)
print('F학점 : %d명' % count_f)