import psutil

# cpu = psutil.cpu_freq()  # cpu의 속도를 출력합니다.
# print(cpu)

cpu_core = psutil.cpu_count(logical=False)  # cpu의 물리 코어 수를 출력합니다.
print(cpu_core)

memory = psutil.virtual_memory()  # 메모리의 정보를 출력합니다.
print(memory)

disk = psutil.disk_partitions()  # 디스크 정보를 출력합니다.
print(disk)

net = psutil.net_io_counters()  # 네트워크를 통해 보내고 받은 데이터 량을 출력합니다.
print(net)