import sqlite3
# 데이터베이스 연결
conn = sqlite3.connect('./data/users.db')
# cursor() 메소드 해당 위치로 이동? 
c = conn.cursor()
# 테이블 생성
c.execute('''DROP TABLE api''')

# 연결된 데이터베이스 변경사항 저장
conn.commit()

# 데이터베이스 연결 종료
conn.close()