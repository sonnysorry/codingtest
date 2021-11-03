def bfs(numbers, root):
    queue = []
    visited = [0 * for _ in range(len(numbers))]
    queue.append(root)
    visited[0] = 1
    while queue:
        node = queue.pop(0)
        for i in range(len(numbers)):
            if numbers[node][i] == 1 and