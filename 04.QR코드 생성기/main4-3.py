import qrcode  # qrcode 모듈을 불러옵니다.
import os  # os 모듈을 불러옵니다.

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 경로를 현재 .py파일이 있는 곳으로 잡아줍니다.

file_path = r"./qr코드모음.txt"  # qr코드를 만들어낼 파일을 지정합니다.
with open(file_path, 'rt', encoding='UTF8') as f :  # file path로 지정해준 파일을 UTF-8로 인코딩해 열어줍니다.
    read_lines = f.readlines()  # f.readlines로 줄별로 값을 읽어 리스트 형태로 read_lines 변수에 바인딩합니다.

    for line in read_lines:  # for문을 통해 read_lines에 저장된 값을 읽어냅니다.
        line = line.strip()  # line.strip은 마지막의 줄바꿈 문자를 삭제합니다.
        print(line)

        qr_data = line  # qr_data 변수에 line 에서 읽은 정보를 저장합니다.
        qr_img = qrcode.make(qr_data)

        save_path = './' + qr_data + '.png'
        qr_img.save(save_path)