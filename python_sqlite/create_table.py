import sqlite3
# 데이터베이스 연결
conn = sqlite3.connect('./data/users.db')
# cursor() 메소드 해당 위치로 이동? 
c = conn.cursor()
# 테이블 생성
c.execute('''CREATE TABLE api (name text, id text, secret text)''')

# 테이블에 데이터 삽입
naver = "INSERT INTO api (name, id, secret) VALUES ('naver_dev','iNWxPWauwZS6dVw9PbOq','WwTBV1lX7H')"
c.execute(naver)
data = "INSERT INTO api (name, secret) VALUES ('public','12mI7L%2FG%2Bl5w1Z1VvsmpBb7ttg7VR7OwYCPao%2BfM0Af3D4JsMJsEuID7DQeFO%2FeLy1AXCYdK%2BrPevDg9WgOX5g%3D%3D')"
c.execute(data)
career = "INSERT INTO api (name, secret)VALUES ('career','b51c4540ebd8a2159ba1ad0609aed569')"
c.execute(career)

# 연결된 데이터베이스 변경사항 저장
conn.commit()

# 데이터베이스 연결 종료
conn.close()