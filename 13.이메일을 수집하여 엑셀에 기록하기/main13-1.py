import re  # 정규 표현식을 사용하기 위해 re 모듈을 불러옵니다.

# 테스트용 문자열을 생성합니다.
test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

# 문자열에서 이메일 형식을 찾아 리스트 형태로 결과를 반환합니다.
results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string) 

print(results)