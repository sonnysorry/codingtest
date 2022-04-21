# 이코테 1 얼음틀

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    if x <= -1 or x >= a or y <= -1 or y >= b:
        return False

    if graph[x][y] == 0:
        for i in range(len(dy)):
            dfs(x + dx[i], y + dy[i])
        return True
    return False

a, b = map(int, input().split())

graph = []
for _ in range(a):
    graph.append(list(map(int, input().split())))

result = 0
for j in range(a):
    for k in range(b):
        if dfs(j, k) == True:
            result += 1
print(result)

