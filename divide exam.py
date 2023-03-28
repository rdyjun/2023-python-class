import random

n = int(input("몇으로 나누는 놀이를 할 까요? : "))
print("Start : %d로 나누어지는 가장 가까운 수로 답하기\n\n" % n)
ans = 0
for i in range(5) :
    num = int(input("Call number = "))

    if num % n == 0 :
        ans = num
    elif num % n > n / 2 :
        ans = num + (n - num % n)
    else :
        ans = num - (num % n)
    print("The answer is %d" % ans)