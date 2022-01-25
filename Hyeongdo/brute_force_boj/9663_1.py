# N-Queen

n = int(input())

chk = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n): 
        if chk[i][j] == 0:
            chk[i][j] = 1