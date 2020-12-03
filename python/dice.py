import random

again = 'y'
count = 1
line = '-' * 30

while again == 'y' :
    print(line)
    print('주사위 던지기 : %d번째' % count)
    me = random.randint(1, 6)
    computer = random.randint(1, 6)
    print('나 : %d' % me)
    print('컴퓨터 : %d' % computer)

    if me > computer :
        print('승리')
    elif me == computer :
        print('무승부')
    else :
        print('패배')

    count = count + 1
    print(line)
    again = input('계속하려면 y를 입력하세요.')