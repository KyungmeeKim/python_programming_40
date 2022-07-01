import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):  # 환율비를 가져오는 함수
    headers = {  # 헤더를 추가합니다. 아무런 헤더 없이 접속하면 로봇이 접속한 것으로 보여 사이트에서 정보를 주지 않습니다. 헤더를 추가해 일반 브라우저를 이용하여 접속한 것처럼 보이게 합니다.
        'User-Agent' : 'Mozilla/5.0', 
        'Content-Type' : 'text/html, charset=utf-8'
    }
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1,target2), headers=headers)  # requests 라이브러리를 이용하여 사이트의 응답값을 가져옵니다.
    content = BeautifulSoup(response.content, 'html.parser')  # BeautifulSoup 라이브러리를 이용해 html로 보기 값을 찾기 좋게 합니다.
    containers = content.find('span', {'data-test': 'instrument-price-last'})  # 마지막 환율 정보를 찾습니다.
    print(containers.text)  # 환율 정보를 출력합니다.


get_exchange_rate('usd', 'krw')  # 위에서 정의한 get_exchange_rate 함수를 이용해 1달러대 원화 비율을 크롤링하여 출력합니다.