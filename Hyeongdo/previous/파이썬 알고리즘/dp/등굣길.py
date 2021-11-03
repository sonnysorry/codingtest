import time
m = 2000
n = 2000
puddles	= [[2, 2]]
def solution(m, n, puddles):
    d = [[0] * m for _ in range(n)]
    d[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0 : continue
            if [j + 1, i+1] in puddles: d[i][j] = 0
            else:
                d[i][j] = d[i][j-1] + d[i-1][j]
    answer = d[n-1][m-1] % 100000007
    return answer
def solution1(m, n, puddles):
    d = [[0] * m for _ in range(n)]
    d[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0 : continue
            if [j + 1, i+1] in puddles: d[i][j] = 0
            else:
                d[i][j] = d[i][j-1] + d[i-1][j]
    answer = d[n-1][m-1] % 1000000007
    return answer
import time
t = time.time()
print(solution(m, n, puddles))
t = (time.time() - t) *1000
print("elapsed time : %.0fms" %t)

t = time.time()
print(solution(m, n, puddles))
t = (time.time() - t) *1000
print("elapsed time : %.0fms" %t)