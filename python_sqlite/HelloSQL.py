# SQLite 라이브러리 사용
import random
import sqlite3
from datetime import datetime
from faker import Faker


def create_users_table(_users):

    # users.db에 새로운 테이블 생성
    conn.execute(
        f'''CREATE TABLE IF NOT EXISTS {_users}(
            id INTEGER PRIMARY KEY, 
            username text, 
            address text,
            postcode text,
            email text,
            tel text,
            city text,
            province text,
            website text,
            reg_time text,
            signin_time text
        )'''
    )

def get_last_id():
    sql_last_row_id = "SELECT IFNULL(Max(id), 0) FROM users "

    # cur = conn.cursor()
    cur.execute(sql_last_row_id)

    rows = cur.fetchall()
    #print(type(rows), rows)
    
    last_id = 0
    for row in rows:
        #print("row type : ", row[0])
        last_id = row[0]
    
    return last_id


def insert_user(
    _id,
    _username,
    _address,
    _postcode,
    _email,
    _tel,
    _city,
    _province,
    _website,
    _reg_time,
    _signin_time):

    # 데이터 삽입
    conn.execute(
        """INSERT INTO users VALUES(
                ?, 
                ?, 
                ?, 
                ?, 
                ?, 
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
        """,                
        [
            _id,
            _username,
            _address,
            _postcode,
            _email,
            _tel,
            _city,
            _province,
            _website,
            _reg_time,
            _signin_time
        ]
    )
    print(f"[{_id}]을 추가했습니다.")


def create_faker_user(num):
    fake = Faker("ko_KR")
    output = [
        {
            "username": fake.name(),
            "address": fake.address(),
            'postcode' : fake.postcode(),
            "email": fake.email(),
            "tel" : fake.phone_number(),
            "city": fake.city(),
            "province": fake.province(),
            "website" : fake.url(),
            "reg_time" : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "signin_time": fake.date_time()
        } #for x in range(num)
    ]
    return output

# main()
#sqlite의 users.db에 연결
conn = sqlite3.connect('./data/users.db')

# 현재 연결한 디비의 데이터 사용위치로 감
cur = conn.cursor()
create_users_table("users")

id = get_last_id()
for i in range(300) :
    # 함수를 이용한 user 추가
    user = create_faker_user(1)[0]

    id = id + 1
    username = user["username"]
    address = user["address"]
    postcode = user["postcode"]
    email = user["email"]
    tel = user["tel"]
    city = user["city"]
    province = user["province"]
    website = user["website"]
    reg_time = user["reg_time"]
    signin_time = user["signin_time"]
    
    insert_user(
        id,
        username,
        address,
        postcode,
        email,
        tel,
        city,
        province,
        website,
        reg_time,
        signin_time
    )

# 여기까지 변경된 내용을 테이블에 입력
conn.commit()

# 중요! 디비 파일 네트워크 등 장치들을 열면 반드시 닫기
conn.close()
