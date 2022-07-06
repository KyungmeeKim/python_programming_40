import threading

def sum(name,value):
    for i in range(0, value):
        print(f"{name} : {i}")  # name과 value를 입력받아 횟수만큼 반복합니다.

t1 = threading.Thread(target=sum, args=('1번 쓰레드', 10))  # t1 쓰레드를 생성합니다. name은 1번 쓰레드, value는 10입니다.
t2 = threading.Thread(target=sum, args=('2번 쓰레드', 10))  # t2 쓰레드를 생성합니다. name은 2번 쓰레드, value는 10입니다.

t1.start
t2.start

print("Main Thread")