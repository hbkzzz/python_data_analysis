i = int(input('숫자를 입력해 주세요 : '))

def even_odd(i) :
    if i % 2 == 0 :
        print('%d은(는) 짝수이다.' % i)
    else :
        print('%d은(는) 홀수이다.' % i)

even_odd(i)