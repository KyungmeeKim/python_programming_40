import socket  # socket 모듈 호출

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket을 연결
in_addr.connect(("www.google.co.kr", 443))  # 443포트를 통해 google에 접속
print(in_addr.getsockname()[0])  # 연결된 소켓 이름 출력 [0]은 ip 주소만 출력하게 함. 없을 경우 포트까지 같이 출력