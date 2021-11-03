import queue
# 재귀를 사용한다.
# bfs는 큐를 사용한다.
def dfs(r, n, adjMat, visited):
    #방문 여부
    visited[r] = True
    #출력
    print(r)
    # 인접행렬 n개의 데이터
    for i in range(n):
        # r에서 i로 가는 간선이 있다면, (방문할 필요가 있는가?)
        if adjMat[r][i] == 1 and not visited[i]:
            # 다시 또 처리를 하자! i에서 출발하는 dfs 또 실행시킨다.
            dfs(i, n, adjMat, visited)

n = int(input())
adjMat = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    adjMat[a-1][b-1] = 1
    adjMat[b-1][a-1] = 1

#dfs
print("dfs")
# false로 초기화
visited = [False]*n
# 초기화, 개수, 인접행렬, 정점 방문
dfs(0, n, adjMat, visited)

#bfs
print("bfs")
visited = [False]*n
queue = queue.Queue()
queue.put(0)
#초기 방
visited[0] = True
#큐가 비어있을 때까지
while not queue.empty():
    #큐에서 헤드 하나 빼냄
    r = queue.get()
    print(r)
    # 이 값이 visited 안에 없으면 큐에 집어넣음.
    for i in range(n):
        if adjMat[r][i] == 1 and not visited[i]:
            queue.put(i)