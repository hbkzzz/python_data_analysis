import requests
from urllib.parse import urlparse
from urllib.parse import quote

header = {}
header["X-Naver-Client-Id"] = "iNWxPWauwZS6dVw9PbOq"
header["X-Naver-Client-Secret"] = "WwTBV1lX7H"


def getData(keyword, start):
    encKeyword = quote(keyword)
    url = 'https://openapi.naver.com/v1/search/blog?query=' + encKeyword
    option = '&display=100' + '&start=' + str(start)

    #result = requests.get(urlparse(url).geturl(),\
    #   headers = {'X-Naver-Client-Id':'iNWxPWauwZS6dVw9PbOq', 'X-Naver-Client-Secret':'WwTBV1lX7H'})

    result =requests.get(
        urlparse(url).geturl(),
        headers=header
    )

    json_obj = result.json()
    return json_obj


def getResultsList(keyword):
    list = []
    for num in range(0, 10):
        # list 안에 키값이 'item' 인 애들만 넣기
        list = list + getData(keyword, num * 100 + 1)['items']
    
    return list

import json

list = []
result1 = getResultsList("서면 맛집")
result2 = getResultsList("자갈치 횟집")
list = list + result1 + result2

file = open("./data/delicious_food.json", "w+") # gangnam.json 파일을 쓰기 가능한 상태로 열기(만들기)
file.write(json.dumps(list)) #쓰기

# Pandas는 여러가지 분석에 유용한 함수들을 제공하여,
# 길고 긴 json 파일을 보다 쉽고 빠르게 파악할 수 있도록 돕는다.
import pandas as pd

df = pd.read_json('./data/delicious_food.json')
print(df.count()) # 각 key 별 숫자 입력

df_sum = df.groupby('bloggername').count() # groupby() 함수를 사용하여 bloggername 별로 출력
print(df_sum)

bloggernames = df['bloggername'] # bloggername 만 출력
print(bloggernames)