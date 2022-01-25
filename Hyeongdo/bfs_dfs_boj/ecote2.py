# 미로탈출

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if x < 1 or y < 1 or x > m or y > n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x, y+1)
        dfs(x+1, y)
        return True
    return False

count = 0
for i in range(1, n):
    for j in range(1, m):
        if dfs(i, j) == True:
            count += 1

print(count)
