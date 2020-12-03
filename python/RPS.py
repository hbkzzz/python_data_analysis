import random

rps_list = ['가위', '바위', '보']

while True :
    rps_in = input('가위(1) / 바위(2) / 보(3) 해당 번호를 입력 : ')
    try :
        input_num = int(rps_in)
        print('')
        print('%s : ' % rps_list[input_num - 1], end = ' ')

        pc_num = random.randint(-3, -1)
        print('%s(PC)' % rps_list[pc_num * (-1) - 1])

        result = input_num + pc_num
        if abs(result) > 1 :
            result *= (-1)

        if result > 0 :
            print('승리\n') 
        elif result < 0 :
            print('패배\n')
        else :
            print('무승부\n다시 입력해주세요 : \n')
    except :
        break