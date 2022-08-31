import os

while True:
    s = input("계산식 입력> ")
    print("결과: {}".format(eval(s)))
    os.system("pause")
