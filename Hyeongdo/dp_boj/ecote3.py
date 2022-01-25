n, m = map(int, input().split())

money_list = []
for _ in range(n):
    money_list.append(int(input()))

d = [10001] * 10001

money_list.sort()
d[0] = 0
for i in range(money_list[0],m+1):
    for k in money_list:
        if d[i-k] != 10001:
            d[i] = min(d[i-k]+1, d[i])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])