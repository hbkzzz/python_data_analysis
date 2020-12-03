# 아직 미완성 코드
import folium
import pandas as pd
import urllib.request
import datetime
import time
import json

def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-NCP-APIGW-API-KEY-ID", "ukr8tyeda9")
    req.add_header("X-NCP-APIGW-API-KEY", "R5IrOFyZJJqwlD16X9QKSjmKLFRvrlCDuYy55HgZ")
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getGeoData(address):
    base = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
    try:
        parameters = "?query=%s" % urllib.parse.quote(address)
    except:
        return None
    
    url = base + parameters
    retData = get_request_url(url)
    if retData == None:
        return None

    jsonAddress = json.loads(retData)
    if 'addresses' in jsonAddress.keys():
        latitude = jsonAddress['addresses'][0]['y']
        longitude = jsonAddress['addresses'][0]['x']
    else:
        return None

    return [latitude, longitude]


def main():
    map = folium.Map(location=[37.5103, 126.982], zoom_start=15)
    filename = './data/csv/서울시 초등학교 현황.csv'
    df = pd.read_csv(filename)
    geoData = []

    for index, row in df.iterrows():
        geoData = getGeoData(row['주소'])
        if geoData != None:
            folium.Marker(geoData, popup=row['학교명'], icon=folium.Icon(color='red', icon='info-sign')).add_to(map)
    
    svFilename = './naver_open_api/elementary_school.html'
    map.save(svFilename)

if __name__ == "__main__":
    main()