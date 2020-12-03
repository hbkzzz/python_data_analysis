name = '안진영'
scores = {'kor':95, 'eng':85, 'math':90, 'science':80}
print(scores)

scores['kor'] = 70
print(scores['kor'])
# 딕셔너리 kor값 수정

scores['music'] = 70
print(scores)
# 딕셔너리 새로 추가

del scores['science']
# print(science)
# 딕셔너리 값에서 삭제

print('이름 : %s' % name)
print('국어 : %d' % scores['kor'])
print('영어 : %d' % scores['eng'])
print('수학 : %d' % scores['math'])