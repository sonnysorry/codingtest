from collections import deque

n = int(input())
k = int(input())

visited = [[0]*n for _ in range(n)]

apple = []
for _ in range(k):
    r, c = map(int, input().split())
    visited[r-1][c-1] = 1

change = {}
lines = int(input())
for _ in range(lines):
    x, c = input().split()
    change[int(x)] = c

snake = deque([[0,0]])
dx = [-1,0,1,0]
dy = [0,1,0,-1]

d= 1
count = 0
nx, ny = 0, 0

def directions(direction):
    if direction == "D":
        d = (d+1) % 4
    else:
        d = (d-1) % 4
    return d

while True:
    count += 1
    nx += dx[d]
    ny += dy[d]

    if count in change.keys():
        d = directions(change[count])

    if (0 <= nx and nx < n and 0 <= ny and ny < n):
        if [nx,ny] in snake:
            break

        if visited[nx][ny] == 1:
            visited[nx][ny] = 0
            snake.append([nx,ny])
        elif visited[nx][ny] == 0:
            snake.append([nx, ny])
            x,y = snake.popleft()
    else:
        break
print(count)


