from gtts import gTTS  #gtts라이브러리에서 gTTS를 불러옵니다.

text = "안녕하세요. 파이썬과 40개의 작품들 입니다." #텍스트 변수에 문장을 바인딩합니다.

tts = gTTS(text=text, lang='ko')  #text 변수의 문자열을 한글로 변환하여 tts 변수에 바인딩합니다.

#r을 붙여 파이썬에서 특별한 명령어로 해석하지 않고, 역슬래쉬 자체로 해석하게 합니다. 
tts.save(r"03.텍스트를 음성으로 변환하기/hi.mp3") #현재 폴더에 hi.mp3 파일이름으로 저장합니다. 
