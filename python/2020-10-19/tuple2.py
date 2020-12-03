tuple1 = ('apple', 'banana', 'cherry')
tuple2 = ('orange', 'melon', 'strawberry')

tuple3 = tuple1 + tuple2
print(tuple3)

print(len(tuple3))

for x in tuple1 :
    print(x)

del tuple1

print(tuple3) # tuple1을 삭제했지만 출력이 됨
print(tuple1) # tuple1을 삭제하여 출력 불가