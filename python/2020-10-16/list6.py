frults = ['apple', 'orange', 'banana']

for frult in frults :
    print(frult)

scores = [88, 75, 90, 95, 77, 69, 80, 92]

sum = 0
length = len(scores)
for score in scores :
    sum += score

avg = sum/length

print('총점 : %d, 평균 : %.2f' % (sum, avg))