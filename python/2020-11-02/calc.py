def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

def mul(a, b) :
    return a * b

def div(a, b) :
    if(b == 0) :
        b = 1
    return a / b

c = add(10, 20)
d = sub(10, 20)
e = mul(10, 20)
f = div(10, 20)

print(f'''
    10 + 20 = {c}
    10 - 20 = {d}
    10 * 20 = {e}
    10 / 20 = {f}
''')