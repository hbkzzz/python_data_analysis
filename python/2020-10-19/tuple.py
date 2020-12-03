# 튜플 에서는 ()로 전체 요소를 감싼다.
menu = ('coffee', 'milk', 'tea', 'cider')

print(menu)
print(menu[0])
print(menu[2])
print(menu[0:3])

menu[1] = 'cola'
# 1의 요소 'milk'를 'cola'로 바꾸는 이 코드는 튜플의 요소를 변경할 수 없어서 에러 메세지가 발생