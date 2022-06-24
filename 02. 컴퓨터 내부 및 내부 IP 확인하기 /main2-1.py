# 단, 가상환경 등을 사용하여 여러개의 환경이 있을 경우 다른 환경의 IP가 출력되거나 정확한 IP를 알 수 없을 수도 있음

import socket  # 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈

in_addr = socket.gethostbyname(socket.gethostname())  # 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩

print(in_addr)
