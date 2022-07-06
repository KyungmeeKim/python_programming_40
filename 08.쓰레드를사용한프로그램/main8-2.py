import threading
import time

def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
t1.daemon = True  # 쓰레드를 데몬 쓰레드로 설정하여 메인동작이 실행될 때에만 쓰레드를 실행하도록 합니다.
t1.start

while True:
    print("메인동작")
    time.sleep(2.0)