import random

random_number = random.randint(1, 100)

"""
random.random()
0.0부터 0.999999 사이의 실수 반환
random.uniform(a, b)
a와 b사이의 실수값을 반환
random.randint(a, b)
a와 b사이의 정수값을 반환
random.randrange(a, b)
a와 b사이의 정수값을 반환
random.randrange(a)
0과 a사이의 정수값을 반환
random.choice(type)
type에는 문자열, 리스트, 튜플, range의 값을 입력받고 무작위 하나의 원소를 뽑음
"""

game_count = 1
while True:
    try:
        my_number = int(input("1 ~ 100 사이의 숫자를 입력하세요:"))

        if (my_number > random_number):
            print("다운")
        elif (my_number < random_number):
            print("업")
        elif (my_number == random_number):
            print(f"축하합니다. {game_count}회 만에 맞췄습니다.")
        
        game_count += 1
    except:
        print("에러가 발생하였습니다. 숫자를 입력하세요")

