# ifconfig.kr 에서 조회하는 외부 IP주소 가져오기

import requests  # 사이트에 접속하기 위한 request 모듈
import re # IP주소를 찾기 위한 정규식을 사용하기 위해 re 모듈을 불러옴 

req = requests.get("http://ipconfig.kr")  # ipconfig 사이트에 접속합니다.
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3})', req.text)[1]  # 정규 표현식을 사용해 ip주소를 가져와 out_addr 변수와 바인딩 합니다.
print(out_addr)  # 외부 ip 주소를 출력합니다.