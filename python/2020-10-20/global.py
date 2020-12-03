def func() :
    global x # 키워드 global은 해당 변수를 전역변수로 사용
    x = 100
    print(x)
    print(id(x))

x = 10
print(x)
func()
print(x)
print(id(x))