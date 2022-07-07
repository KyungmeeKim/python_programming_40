import googletrans  # googletrans를 불러옵니다. 

translator = googletrans.Translator()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='auto')  # dest: 번역될 문자를 입력합니다. src: 번역할 문자의 언어로 auto가 기본입니다.
print(f"행복하세요 => {result1.text}")

str2 = "I am happy"
result2 = translator.translate(str2, dest='ko', src='en')
print(f"I am happy => {result2.text}")