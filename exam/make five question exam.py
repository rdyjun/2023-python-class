import random

correct = False
i = 0
score = 0

x = random.randint(10, 99)
y = random.randint(10, 99)

while i < 5 and not correct :
    print("%d + %d = " % (x, y), end = '')
    ans = int(input())
    if ans == x + y :
        print("Collect!!!")
        correct = True
        score += (20 - i * 3)
    else :
        print("TryAgain---")
    i += 1

        