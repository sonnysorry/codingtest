# 정수삼각형
def solution(triangle):
    dp = triangle
    for i in range(2, len(dp)):
        for j in range(i+1):
            if j != 0 and i != j:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
            elif j == 0:
                dp[i][j] += dp[i-1][j]
            elif i == j:
                dp[i][j] += dp[i-1][j-1]
    answer = sum(dp[len(dp)]) + 7
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))