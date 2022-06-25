import socket  # 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈

in_addr = socket.gethostbyname(socket.gethostname())  # 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩

print(in_addr)
