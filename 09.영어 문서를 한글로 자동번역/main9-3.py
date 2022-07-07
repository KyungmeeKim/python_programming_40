from os import linesep
import googletrans
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 현재 파이썬 파일로 경로를 변경해줍니다.

translator = googletrans.Translator()

read_file_path = r"./영어파일.txt"  # 파일을 읽어올 경로를 지정합니다.

with open(read_file_path, 'r') as f:
    readLines = f.readlines()  # 파일에서 줄별로 읽어 readLines에 리스트 형태로 바인딩합니다.

for lines in readLines:  # 리스트 형태로 저장된 readLines에서 한 줄 씩 한글로 변환하여 출력합니다.
    result1 = translator.translate(lines, dest='ko') 
    print(result1.text)