# 구구단
'''
dan_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for dan in dan_number :
  print("현재 단수 : ", dan)
  for item in number :
    print(dan, " * ", item, " = ", dan * item)
'''

# 19단 만들기
for a in range(1, 20) :
    for b in range(1, 10) :
        print(f'{a} X {b} = {a * b}', end='\t')
    print()