hello = '안녕' * 5

print(hello)

# len() 함수 문자열 길이 구하기
a = '쥐 구멍에 볕 들 날 있다.'

b = len(a)

c = ''
d = ' '

e = len(c)
f = len(d)

print(b)
print(e)
print(f)

name = '홍길동'
greet = name + '님 안녕하세요!'
print(greet)

# 문자열을 연결할 때 연결대상이 모두 문자열이여야 한다
# 잘못된 예
# eng = 80
# result = '영어점수 : ' + eng + '점'
# print(result)

eng = 80
kor = 90
result = '영어 점수 : ' + str(eng) + '점'
result2 = '국어 점수 : ' + str(kor) + '점'
print(result)
print(result2)