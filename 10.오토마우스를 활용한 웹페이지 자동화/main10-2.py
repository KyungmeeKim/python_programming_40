import pyautogui
import time
import pyperclip

pyautogui.moveTo(1168, 220, 0.2)  # 네이버 검색 좌표로 0.2초 동안 이동합니다.
pyautogui.click()  # 클릭합니다
time.sleep(0.5)  # 0.5초 기다립니다

pyperclip.copy("서울 날씨")  # 클립보드에 "서울날씨"를 저장합니다.
pyautogui.keyDown("command") # 클립보드에 저장된 내용을 붙여넣습니다.
pyautogui.press('v')
pyautogui.keyUp("command")
time.sleep(0.5)  # 0.5초 기다립니다.

pyautogui.write(["enter"])  # 엔터키를 입력합니다
time.sleep(1)  # 1초동안 기다립니다