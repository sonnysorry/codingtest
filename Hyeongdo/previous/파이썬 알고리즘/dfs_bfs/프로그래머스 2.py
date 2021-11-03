answer = 0
def dfs(n, computers, depth):
    global answer
    visit[depth] = 1
    answer += 1
    for i in range(n):
        if computers[depth][i] == 1 and visit[i] == 0:
            dfs(n, computers, i)

def solution(n, computers):
    global answer
    dfs(n, computers, 1)
    return answer

n = 3
visit = [0 for _ in range(n)]

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))