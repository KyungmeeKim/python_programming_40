from gtts import gTTS
from playsound import playsound  #playsound 모듈에서 playsound를 불러와 사용합니다.
import os  #경로를 이동하기 위해 os 라이브러리를 불러옵니다.

os.chdir(os.path.dirname(os.path.abspath(__file__)))  #경로를 현재 main3-2.py를 실행하는 경로로 이동합니다. playsound에서 경로를 인식하지 못하기 때문에 현재 경로로 이동합니다.

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("./hi.mp3")