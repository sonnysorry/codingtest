# 회의실 배정

n = int(input())
con = [list(map(int, input().split())) for _ in range(n)]

# 2차원 배열 정렬 
con.sort(key=lambda x:(x[1], x[0]))

temp = 0
count = 0
for i in range(0, n):
    if con[i][0] >= temp:
        temp = con[i][1]   
        count += 1

print(count)