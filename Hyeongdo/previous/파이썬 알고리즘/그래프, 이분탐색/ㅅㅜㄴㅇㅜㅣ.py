n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n, results):
    win = dict()
    lost = dict()
    for a, b in results:
        win.setdefault(a, []).append(b)
        lost.setdefault(b, []).append(a)
    print(win)
    print(lost)
    queue = [1]
    visited = [0 for _ in range(n)]
    while queue:
        a = queue.pop(0)
        for i in range(1, n + 1): v
            if not i in win.keys():
                continue
        if visited[i] == 0 and win.keys(i) == a:
            print(visited[i])


print(solution(n, results))