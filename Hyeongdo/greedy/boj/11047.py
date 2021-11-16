#동전 0
n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins = sorted(coins, reverse=True)

count = 0

for c in coins:
    if c <= k:
        count += k//c
        k %= c

print(count)
        