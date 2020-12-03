import requests
import bs4

endpoint = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
serviceKey = "12mI7L%2FG%2Bl5w1Z1VvsmpBb7ttg7VR7OwYCPao%2BfM0Af3D4JsMJsEuID7DQeFO%2FeLy1AXCYdK%2BrPevDg9WgOX5g%3D%3D"
numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "15"
areaCode = "1"
sigunguCode = "4"
listYN = "Y"

paramset = "serviceKey=" + serviceKey + "&" + "numOfRows=" + numOfRows + "&" + "pageSize=" + pageSize + \
    "&" + "pageNo=" + pageNo + "&" + "MobileOS=" + MobileOS + "&" + "MobileApp=" + MobileApp + \
    "&" + "arrange=" + arrange + "&" + "contentTypeId=" + contentTypeId + "&" + "areaCode=" + areaCode + \
    "&" + "sigunguCode=" + sigunguCode + "&" + "listYN=" + listYN

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
print(bs_obj.findAll("title"))