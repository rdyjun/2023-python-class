import random as rd

lotto = set()

while True:
    num = rd.randrange(1, 46)
    print(num, end=' ')
    lotto.add(num)
    if len(lotto) == 6 :
        break
print("\n 집합 : {}", format(lotto))
print("\n 정렬리스트 : {}", sorted(lotto))  # lotto는 바뀌지 않음

print("\n sample로 번호리스트 만들기")
lt = rd.sample(range(1, 46), 6)
print("\n sample 함수 리스트 : ", format(lt))
print("\n sample 함수 정렬리스트 : ", format(sorted(lt)))
