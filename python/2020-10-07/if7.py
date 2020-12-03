nowyear = int(input('현재년을 입력해 주세요 : '))
nowmonth = int(input('현재월을 입력해 주세요 : '))
nowday = int(input('현재일을 입력해 주세요 : '))

birthyear = int(input('출생년을 입력해 주세요 : '))
birthmonth = int(input('출생월을 입력해 주세요 : '))
birthday = int(input('출생일을 입력해 주세요 : '))

if birthmonth < nowmonth :
    age = nowyear - birthyear
elif birthmonth == nowmonth :
    if birthday < nowday :
        age = nowyear - birthyear
    else :
        age = nowyear - birthyear - 1
else :
    age = nowyear - birthyear - 1

print('-' * 50)
print('오늘 날짜 : %d년 %d월 %d일' % (nowyear, nowmonth, nowday))
print('생년 월일 : %d년 %d월 %d일' % (birthyear, birthmonth, birthday))
print('-' * 50)
print('만 나이 : %d세' % age)
print('-' * 50)