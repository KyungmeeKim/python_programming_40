import os
import readline
import googletrans

os.chdir(os.path.dirname(os.path.abspath(__file__)))

translator = googletrans.Translator()

read_file_path = r"./영어파일.txt"
write_file_path = r"./한글파일.txt"

with open(read_file_path,'r') as f :
    readLines = f.readlines()


for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path,'a',encoding='UTF8') as f:  # 파일을 저장합니다. 'a'옵션은 마지막에 추가로 쓰는 모드입니다.
        f.write(result1.text + '\n')


