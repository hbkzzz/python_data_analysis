dans = (2,3,4,5,6,7,8,9)
rows = (1,2,3,4,5,6,7,8,9)

print('구구단표')
print('-' * 30)

for dan in dans :
    for i in rows :
        print('%d x %d = %d' % (dan, i, dan*i))
    print('-' * 30)