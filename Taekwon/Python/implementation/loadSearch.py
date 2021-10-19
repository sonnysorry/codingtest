# 못 푼 문제 시간복잡도가 높음..
n = int(input())
data = list(input().split())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x = 1
y = 1

for i in data:
    if x <= 0 or x >= n or y <= 0 or y >= n:
        continue
    if i == 'R':
        x += dx[0]
        y += dy[0]
    if i == 'U':
        x += dx[1]
        y += dy[1]
    if i == 'L':
        x += dx[2]
        y += dy[2]
    if i == 'D':
        x += dx[3]
        y += dy[3]
print(x, y)
