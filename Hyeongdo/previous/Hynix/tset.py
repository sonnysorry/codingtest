
n, k = map(int, input().split())
arr = [list(map(int, input().split()) for _ in range(n))]
dp = [0] * 100

for i in range(n):
    for j in range(k, 0, -1):
        if (arr[i][0] <= j):
            dp[j] = max(dp[j], dp[j-w[i]] + p[i])

print(dp[k])