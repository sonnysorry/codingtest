def solution(n, computers):
    queue = []
    visited = [0 for _ in range(n)]
    answer = 0
    while 0 in visited:
        a = visited.index(0)
        queue.append(a)
        visited[a] = 1
        while queue:
            node = queue.pop(0) # 2
            for i in range(n):
                if computers[node][i] == 1 and visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
        answer += 1
    return answer
print(bfs(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))