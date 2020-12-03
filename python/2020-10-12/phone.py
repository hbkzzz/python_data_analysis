# 전화번호에서 하이픈(-) 추가하기

phone = input('하이픈(-)을 뺀 11자리의 휴대폰 번호를 입력하세요 : ')
num = ''

for i in range(0, len(phone)) :
    if i == 2 :
        num = num + (phone[2]+'-')
    elif i == 6 :
        num = num + (phone[6]+'-')
    else :
        num = num + phone[i]

print(num)