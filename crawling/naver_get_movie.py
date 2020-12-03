from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import json
import re
import requests
from io import BytesIO
from PIL import Image

# 네이버 검색 Open API 사용 요청시 얻게되는 정보를 입력
client_id = "iNWxPWauwZS6dVw9PbOq"
client_secret = "WwTBV1lX7H"


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def searchByTitle(title):
    url = 'https://openapi.naver.com/v1/search/movie.json?display=100&query=' + quote(title)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        d = json.loads(response_body.decode('utf-8'))
        if(len(d['items']) > 0):
            return d['items'] 
        else:
            return None
    else:
        print("Error Code:" + rescode)


def findItemByInput(items):
    for index, item in enumerate(items):
        navertitle = cleanhtml(item['title'])
        naversubtitle = cleanhtml(item['subtitle'])
        naverpubdate = cleanhtml(item['pubDate'])
        naveractor = cleanhtml(item['actor'])
        naverlink = cleanhtml(item['link'])
        naveruserScore = cleanhtml(item['userRating'])

        navertitle1 = navertitle.replace(" ", "")
        navertitle1 = navertitle1.replace("-", ",")
        navertitle1 = navertitle1.replace(":", ",")

        #기자 평론가 평점을 얻어 옵니다.
        spScore = getSpecialScore(naverlink)

        # 네이버가 다루는 여화 고유 ID를 얻어옵니다
        naverid = re.split("code=", naverlink)[1]

        # 영화의 타이틀 이미지를 표시 합니다.
        #if(item['image'] != None and "http" in item['image']):
        #    response = requests.get(item['image'])
        #    img = Image.open(BytestIO(response.content))
        #    img.show()
    
        print(index, navertitle, naversubtitle, naveruserScore, spScore)


def get_soup(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    return soup


# 기자 평론가 평점을 얻어 옵니다
def getSpecialScore(URL):
    soup = get_soup(URL)
    scorearea = soup.find_all('div', 'spc_score_area')
    newsoup = BeautifulSoup(str(scorearea), 'lxml')
    score = newsoup.find_all('em')
    if(score and len(score) > 5):
        scoreis = score[1].text + score[2].text + score[3].text + score[4].text
        return float(scoreis)
    else:
        return 0.0


def getInfoFromNaver(searchTitle):
    items = searchByTitle(searchTitle)
    if(items != None):
        findItemByInput(items)
    else:
        print("No result")

# 진입점 함수를 main으로 지정
if __name__ == '__main__':
    getInfoFromNaver(u"미션")
