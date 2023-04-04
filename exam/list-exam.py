import random as rd

list = []

for i in range(20) :
    num = rd.randrange(0, 100)
    if(list.count(num) == 0) :
        list.append(num)

list.sort()

n = int(input("몇 번째 데이터를 원하시나요?"))
print(list[n])
