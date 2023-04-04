menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거', '새우버거')
price = (4000, 4500, 5000, 7000, 5500)
mdict_list = []

for i in range(len(menu)) :
    mdict_list.append([menu[i], price[i]])

n = 1

for i in range(len(menu)) :
    print(i, " : ", menu[i], " : ", price[i])

print("메뉴: ", menu)
print("가격: ", price)
print("딕", mdict_list)