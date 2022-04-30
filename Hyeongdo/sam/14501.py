
n = int(input())

t = []
p = []
dp = [0]*(n+1)

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
for i in range(n-1, -1, -1):
    if i+t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[i+t[i]], dp[i+1])
print(dp[0])

