import random
import os

def input_check(msg,casting=int):
    while True:
        try:
            user_input = casting(input(msg))
            return user_input
        except:
            print("잘못입력하셨습니다. 숫자만 입력해라")
            continue


chance = 10
count = 0

number = random.randint(1,99)
os.system("cls")
print("1부터 99까지의 숫자를 10번 안에 맞춰보세요.")

while count < chance:
    count += 1
    user_input = input_check("몇 일까요?")

    if number == user_input:
        break
    elif user_input == 0:
        print("프로그램을 종료합니다.")
        quit()
    elif user_input < number:
        print("{} 보다 큰 숫자입니다.".format(user_input))
    elif user_input > number:
        print("{} 보다 작은 숫자입니다.".format(user_input))

if user_input == number:
    print("성공! {}이 맞습니다.".format(number))
else:
    print("실패! 정답은 {}입니다.".format(number))