from tracemalloc import start
from numpy import save
import pyautogui
import time
import pyperclip
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) 

weather = ['서울날씨', '시흥날씨', '부산 날씨', '대전 날씨', '강원도 날씨']

addr_x = 141
addr_y = 668
start_x = 992
start_y = 220
end_x = 1656
end_y = 635


for r_weather in weather:
    pyautogui.moveTo(addr_x, addr_y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(r_weather)
    pyautogui.keyDown("command") # 클립보드에 저장된 내용을 붙여넣습니다.
    pyautogui.press('v')
    pyautogui.keyUp("command")
    time.sleep(0.5)  # 0.5초 기다립니다.

    pyautogui.write(["enter"])  # 엔터키를 입력합니다
    time.sleep(1)  # 1초동안 기다립니다

    savepath = './' + r_weather + '.png'
    pyautogui.screenshot(savepath, region=(start_x, start_y, end_x-start_x, end_y-start_y))