#가장 긴 바이토닉 부분 수역

n = int(input())
num_list = list(map(int, input().split()))

dp1 = [1]*(n+1)
dp2 = [1]*(n+1)


for i in range(1,n):
    for j in range(0,i):
        if num_list[i] > num_list[j]:
            dp1[i] = max(dp1[j]+1, dp1[i])

for k in range(n-1, 0, -1):
    for p in range(n-1, k, -1):
        if num_list[k] > num_list[p]:
            dp2[k] = max(dp2[p]+1, dp2[k])

dp3 = [1]*(n+1)
for u in range(len(dp1)):
    dp3[u] = dp1[u] + dp2[u]

answer = max(dp3)
print(answer-1)