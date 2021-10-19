row, col = map(int, input().split())
n, m, d = map(int, input().split())

data = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir_types = [0, 1, 2, 3] #북동남서


for i in range(row):
    i = list(map(int, input().split()))
    data.append(i)
