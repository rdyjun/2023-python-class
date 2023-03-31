import random

randInt = random.randrange(1, 21)

while (True) :
    user = int(input("1부터 20사이의 수를 입력하세요"))
    if user > 0 and user <= 20 :
        if user == randInt :
            print("맞았습니다 !")
            break;
        elif user > randInt :
            print("입력하신 값이 정답보다 큽니다.")
        elif user < randInt :
            print("입력하신 값이 정답보다 작습니다")
    else :
        print("값이 올바르지 않습니다.")