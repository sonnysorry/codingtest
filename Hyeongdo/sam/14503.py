from collections import deque

n, m = map(int,input().split())

r,c,d = map(int, input().split())

num_list = []
for _ in range(n):
    num_list.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1
count = 1

while True:
    flag = 0
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and num_list[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                r = nx
                c = ny
                flag = 1
                break
    if flag == 0:
        if num_list[r-dx[d]][c-dy[d]] == 1:
            print(count)
            break
        else:
            r, c = r-dx[d], c-dy[d]

