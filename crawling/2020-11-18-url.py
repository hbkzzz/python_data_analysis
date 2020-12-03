# urllib.parse 패키지 전체를 추가 하지 않고 quote함수만 사용
from urllib.parse import quote

city = "부산"
print(city)

city = quote(city)
print(city)