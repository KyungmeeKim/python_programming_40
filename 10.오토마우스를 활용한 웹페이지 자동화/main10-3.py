import pyautogui
import time
import pyperclip
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) 

pyautogui.moveTo(419, 211, 1.0)  # 네이버 검색 좌표로 1초 동안 이동합니다.
pyautogui.click()  # 클릭합니다
time.sleep(0.5)  # 0.5초 기다립니다

pyperclip.copy("서울 날씨")  # 클립보드에 "서울날씨"를 저장합니다.
pyautogui.keyDown("command") # 클립보드에 저장된 내용을 붙여넣습니다.
pyautogui.press('v')
pyautogui.keyUp("command")
time.sleep(0.5)  # 0.5초 기다립니다.

pyautogui.write(["enter"])  # 엔터키를 입력합니다
time.sleep(1)  # 1초동안 기다립니다

start_x = 284
start_y = 133
end_x = 674
end_y = 786

pyautogui.screenshot(r"./서울날씨.png", region=(start_x, start_y , end_x-start_x, end_y-start_y))