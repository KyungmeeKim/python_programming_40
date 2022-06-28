import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1) # cpu 사용량의 1초동안의 평균 값을 구합니다. 1초 동안 측정한 후 다음 줄로 이동합니다.
    print(f"cpu사용량: {cpu_p}%")  # cpu의 사용량을 출력합니다.

    memory = psutil.virtual_memory()  # 사용가능한 메모리를 출력합니다.
    memory_avail = round(memory.available/1024**3, 1)
    print(f"사용 가능한 메모리:{memory_avail}GB")

    net = psutil.net_io_counters()  # 네트워크에서 보내고 받은 크기를 출력합니다.
    curr_sent = net.bytes_sent/1024**2 
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent,1)  # 현재 측정한 값에서 이전에 측정한 값을 빼서 1초동안 보내는 데이터를 구합니다.
    recv = round(curr_recv-prev_recv,1)

    print(f'보내기: {sent}MB 받기: {recv}MB')

    prev_sent = curr_sent  # 이전의 값에 현재 값을 바인딩합니다.
    prev_recv = curr_recv
