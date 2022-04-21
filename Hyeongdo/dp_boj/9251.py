
a = input()
b = input()

dp = [[0]*1002 for _ in range(1002)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)][len(b)])


