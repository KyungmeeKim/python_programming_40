import qrcode  #qr코드 라이브러리를 불러옵니다.
import os # os 라이브러리를 불러옵니다.

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 경로를 현재 .py파일을 실행하는 경로로 이동합니다.


qr_data = "www.naver.com"  # qr_data 변수에 naver.com의 주소를 바인딩 합니다.
qr_img = qrcode.make(qr_data)  # qr_data값을 qrcode.make로 이미지를 만들어 qr_img 변수에 바인딩 합니다.

save_path = './' + qr_data +".png"  #save_path변수에 저장될 경로를 바인딩 합니다.
qr_img.save(save_path)  # 이미지를 저장합니다.