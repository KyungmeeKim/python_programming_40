# 내부, 외부 IP 주소 한꺼번에 출력하는 프로그램
import socket
import requests
import re

# 내부 IP 출력하기
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP 주소 : " , in_addr.getsockname()[0])

# 외부 IP 출력하기
req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP 주소 : ", out_addr)