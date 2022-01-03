# 수들의 합

s = int(input())
tmp = 4294967295

n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)