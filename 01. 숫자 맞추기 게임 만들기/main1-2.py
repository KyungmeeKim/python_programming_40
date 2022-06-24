# 1-1 반복문 추가

import random

random_number = random.randint(1,100)

game_count = 1  # 입력횟수를 세기 위한 game_count 변수를 생성하고 1의 값을 대입합니다.


while True:  # while 조건문으로 break를 만나기 전까지 계속 반복합니다.
    my_number = int(input("1 ~100 사이의 숫자를 입력하세요:"))  # 입력받은 값의 타입을 int형으로 변환하여 my_number 변수와 바인딩 합니다.

    if my_number > random_number:  # 입력한 숫자가 임의 생성 숫자보다 클 경우 '다운'을 출력합니다.
        print('다운')
    if my_number < random_number: # 입력한 숫자가 임의 생성 숫자보다 작을 경우 '업'을 출력합니다.
        print('업')
    elif my_number == random_number:  # 입력한 숫자가 임의 생성 숫자와 같을 경우 game_count 횟수와 문구를 출력하고, 반복문에서 벗어납니다.
        print(f'축하합니다! {game_count}회 만에 정답입니다.')
        break

    game_count += 1  # 조건문이 1번 돌 때마다 game_count를 1회씩 증가시킵니다.