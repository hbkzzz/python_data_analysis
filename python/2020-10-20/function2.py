# 1부터 100까지의 합계
def print_sum() :
    from_i = 1
    to_i = 100
    sum = 0

    for i in range(from_i, to_i + 1) :
        sum += i
        print("i = %d, sum = %d" % (i, sum))

    return sum
print_sum()

# 원하는 부분까지 합계
def print_sum_param(_from, _to) :
    from_i = _from
    to_i = _to
    sum = 0

    for i in range(from_i, to_i + 1) :
        sum += i
        print("i = %d, sum = %d" % (i, sum))

print_sum_param(1, 1000)

# 원하는 부분까지 합구하고 결과값 돌려주기
def sum_param(_from, _to) :
    from_i = _from
    to_i = _to
    sum = 0

    for i in range(from_i, to_i + 1) :
        sum += i
        print("i = %d, sum = %d" % (i, sum))

    return sum

calc_sum = sum_param(1,100)
print("1 + ... + 100 = %d" % calc_sum)