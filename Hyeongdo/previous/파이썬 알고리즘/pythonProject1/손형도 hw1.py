n, k = map(int, input().split())
chk = []
for i in range(k):
    a = int(input("입력 : "))
    chk.append(a)
sum_2 = []
for p in range(k):
    for j in range(1, n+1):
        if (j % chk[p] == 0):
            sum_2.append(j)
sum_1 = list(set(sum_2))
num = sum(sum_1)
print(num)

