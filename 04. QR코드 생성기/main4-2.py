import qrcode
import os # os 라이브러리를 불러옵니다.

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 경로를 현재 .py파일을 실행하는 경로로 이동합니다.

file_path = r'./qr코드모음.txt'  # qr코드모음 파일을 읽습니다.
with open(file_path, 'rt', encoding='UTF8') as f :  # f.readlines()로 파일을 읽어 줄 별로 리스트 값의 형태로 내어줍니다.
    read_lines = f.readlines() # f.readlines()로 파일을 읽어 줄 별로 리스트 값의 형태로 내어줍니다. read_lines에는 줄별로 읽힌 값이 리스트 형태로 바인딩 됩니다.

    for line in read_lines:  # for문으로 전체 문장을 읽습니다.
        line = line.strip()  # line.strip()은 마지막 줄바꿈 문자를 삭제합니다.
        print(line)  # 값을 출력합니다.