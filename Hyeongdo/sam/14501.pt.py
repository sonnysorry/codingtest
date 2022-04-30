"""
오늘부터 n+1일에 퇴사하므로 n일간 최대한 많이 상담
완료 시간 : ti
각 금액 : pi
최대 금액
dp 구나~
"""
n = int(input())
t_list = []
p_list = []
dp = [0]*n
for _ in range(n):
    a, b = map(int,input().split())
    t_list.append(a)
    p_list.append(b)

for i in range(n-1, -1, -1):
    if t_list[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p_list[i] + dp[i+t_list[i]])
print(dp[0])




