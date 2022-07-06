import threading  # thread(코드를 실행하는 하나의 동작) 모듈을 불러옵니다.
import time

def thread_1():  # thread_1의 함수로 1초에 한번씩 "쓰레드1 동작"을 출력합니다.
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)  # 쓰레드를 설정합니다.
t1.start()  # 쓰레드를 시작합니다.

while True:  # 메인코드로 "메인동작"을 2초마다 출력합니다.
    print("메인동작")
    time.sleep(2.0)