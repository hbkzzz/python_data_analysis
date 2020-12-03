# 전화번호에서 하이픈(-) 삭제하기

num = input('하이픈(-)을 포함한 휴대폰 번호를 입력하세요 : ')

for x in num :
    if x != '-' :
        print('%s' % x, end='')