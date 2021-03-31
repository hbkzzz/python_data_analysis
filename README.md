# Python Data Analytics
> Python
>> Data Analytics
>>> Machine Learning
## 파이썬이란 무엇인가?
파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, 플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. 
파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python's Flying Circus〉에서 따온 것이다.
파이썬은 비영리의 파이썬 소프트웨어 재단이 관리하는 개방형, 공동체 기반 개발 모델을 가지고 있다.
C언어로 구현된 사이썬 구현이 사실상의 표준이다.
## 목표
1. 파이썬 기초 프로그래밍
2. 가상환경을 사용한 파이썬 버전 및 패키지 관리
3. 빅데이터 개념 및 특징 이해 
4. 데이터 분석 및 시각화 
5. 크롤링 이해 및 데이터 추출
6. 통계분석 방법
***
## 개발환경 구축
* [Anaconda3](https://www.anaconda.com/products/individual)
* [Java](https://www.java.com/ko/download/)
* [Visual Studio](https://visualstudio.microsoft.com/ko/downloads/)
* [Visual Studio Code](https://code.visualstudio.com/)
## 개발환경 참조
* 현재 문서 기준 Window, 파이썬 3.8.5버전, 자바 8버전 사용
* 아나콘다 설치시 path추가 옵션 체크(체크시 글자가 빨간색으로 바뀜)
* path추가 체크 안했다면 anaconda3, anaconda3\envs 환경변수 추가
* Java\jre, Java\jre\bin 환경변수 추가
* Visual Studio 커뮤니티 설치 → C++ 이용한 데스크톱 개발 체크 후 설치
***
## Anaconda3 명령어
|내용|명령 프롬프트 입력|
|:---:|:---:|
|아나콘다 설치된 버전 확인|conda --version|
|아나콘다 최신버전 업데이트|conda update conda|
|파이썬 3.8버전 data 가상환경 추가|conda create --name data python=3.8|
|data 가상환경 삭제|conda remove --name data --all|
|가상환경 목록 확인|conda info --envs|
|가상환경 data 활성화|conda activate data|
|가상환경 data 비활성화|conda deactivate data|
## 파이썬 패키지 및 라이브러리 명령어 모음
|내용|명령 프롬프트 입력|
|:---:|:---:|
|설치된 패키지 확인|pip freeze 또는 pip list|
|패키지의 정보 확인|pip show 패키지명|
|패키지 설치|pip install 패키지명|
|패키지 삭제|pip uninstall 패키지명|
|패키지 특정버전 설치|pip install 패키지명=버전|
|패키지 최신버전 업그레이드|pip install -U(또는 --upgrade) 패키지명|
|XlsxWriter|pip install xlsxwriter|
|Jupyter|pip install jupyter|
|Matplotlib|pip install matplotlib|
|Numpy|pip install numpy|
|Pandas|pip install pandas|
|Faker|pip install faker|
|Folium|pip install folium|
|Lxml|pip install lxml|
|BeautifulSoup4|pip install beautifulsoup4|
|Requests|pip install requests|
|KoNLPy|pip install konlpy|
|JPype1|pip install jpype1|
|pytagcloud|pip install pytagcloud|
|Pygame|pip install pygame|
|simplejson|pip install simplejson|
|xlrd|pip install xlrd|
## Exel 관련 라이브러리
* [xlwt](https://pypi.org/project/xlwt/)
* [OpenPyXL](https://openpyxl.readthedocs.io/en/latest/)
* [XlsxWriter](https://xlsxwriter.readthedocs.io/)
* [PyExcelerate](https://github.com/kz26/PyExcelerate/)
## Open API 에러 모음
|에러코드|에러메세지|설명|
|:---:|:---:|:---:|
|0|NORMAL_CODE|정상|
|1|APPLICATION_ERROR|어플리케이션 에러|
|2|DB_ERROR|데이터베이스 에러|
|3|NODATA_ERROR|데이터베이스 없음 에러|
|4|HTTP_ERROR|HTTP 에러|
|5|SERVICETIMEOUT_ERROR|서비스 연결실패 에러|
|10|INVALID_REQUEST_PARAMETER_ERROR|잘못된 요청 파라메터 에러|
|11|NO_MANDATORY_REQUEST_PARAMETERS_ERROR|필수요청 파라미터 없음|
|12|NO_OPENAPI_SERVICE_ERROR|해당 오픈API서비스가 없거나 폐기됨|
|20|SERVICE_ACCESS_DENIED_ERROR|서비스 접근거부|
|22|LIMITED_NUMBER_OF_SERVICE_REQUESTS_EXCEEDS_ERROR|서비스 요청제한횟수 초과에러|
|30|SERVICE_KEY_IS_NOT_REGISTERED_ERROR|등록되지 않은 서비스키|
|31|DEADLINE_HAS_EXPIRED_ERROR|기한만료된 서비스키|
|32|UNREGISTERED_IP_ERROR|등록되지 않은 IP|
|33|UNSIGNED_CALL_ERROR|서명되지 않은 호출|
|99|UNKNOWN_ERROR|기타에러|
***
## XlsxWriter 에러 디버깅
* 2020년 10월 기준 anaconda3 기본 가상환경에 설치된 1.2.9 버전이 호환성 문제로 실행시 에러 발생
* 삭제 후 다시 라이브러리 설치 혹은 새로운 가상환경 만들고 설치
## SQLite 참조
* URL : https://sqlitebrowser.org/
* Sample Download : https://www.sqlitetutorial.net/sqlite-sample-database/
## 웹 개발 참조
* URL : https://www.w3schools.com
## 나눔고딕 폰트 관련
###### 네이버 나눔고딕 : http://hangeul.naver.com/webfont/NanumGothic/NanumGothic.ttf
1. anaconda3\envs\{가상환경}\Lib\site-packges\pytagcloud\fonts 으로 이동
2. ttf파일을 넣고 코드에디터 재실행 
3. 그래도 실행 안될시 아래 조치법까지 참조
4. {가상환경}\Lib\site-packges\pytagcloud\fonts 폴더 안에 font.json 마지막 리스트안에 아래 코드 추가
5. ,{ "name": "NanumGothic", "ttf": "NanumGothic.ttf", "web": "http://fonts.googleapis.com/css?family=Nanum+Gothic" }
## 한글 파라미터 URL 변환 참조
* 한글 파라미터를 사용하는 경우 내부적으로 직접 코드 작성 필요 하지만 변환기능을 제공하는 사이트도 있다
* URL : https://www.urlencoder.org/
## 웹크롤링 에러 디버깅
* jpyp1 설치 후에 실행이 안되고 에러 발생이 많은데 아래 주소 참조하거나 해당 에러 메세지 검색 
* URL : http://konlpy.org/ko/latest/install/
## Folium 에러 디버깅
* import 실패시 conda install -c conda-forge folium 입력
## 네이버 지도 참조
* URL : https://apidocs.ncloud.com/ko/ai-naver/maps_geocoding/geocode/
