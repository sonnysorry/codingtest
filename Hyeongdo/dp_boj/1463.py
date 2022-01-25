# 1로 만들기



n = int(input())
dp = [0 for _ in range(1000000)]

count = 0
for i in range(1, 1000000):
    dp[0] = n
    if dp[i-1] == 1:
        break

    if dp[i-1] % 3 == 0:
        dp[i] = dp[i-1] // 3 
        count += 1
    elif dp[i-1] % 2 == 0:
        dp[i] = dp[i-1] // 2
        count += 1
    else:
        dp[i] = dp[i-1] - 1
        count += 1

for i in range(10):
    print(dp[i])
print(count)