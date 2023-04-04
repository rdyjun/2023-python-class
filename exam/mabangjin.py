n = int(input("마방진 사이즈 입력 : "))

table = [[0] * n for k in range(n)]

i = 0
j = n // 2
table[i][j] = 1
count = 2
while count <= n * n :
    row = i - 1
    col = j - 1
    if row < 0 :
        row = n - 1
    if col < 0 :
        col = n - 1
    if table[row][col] != 0 :
        i += 1
    else :
        i = row
        j = col
    table[i][j] = count
    count += 1

print("magic number = ", sum(table[0]))
for row in table :
    print(row)
print("--------------------------")

for i in table :
    for k in i :
        print("%4d" % k, end='')
    print("\n")