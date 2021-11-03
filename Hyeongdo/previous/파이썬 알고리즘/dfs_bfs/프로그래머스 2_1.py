def bfs(computers, n):
    answer = 0
    # 탐색을 위한 큐 생성
    queue = []
    # 방문한 노트 체크하는 리스트 생성
    visited = [0 for _ in range(n)]
    # 큐에 초기 인덱스 0 추가
    queue.append(0)
    # 체크 리스트의 첫번째 위치에 1 체크
    visited[0] = 1
    # visited list 안의 0에서
    while 0 in visited:
        x = visited.index(0)
        queue.append(x)
        visited[x] = 1
        # 큐가 empty 가 이닐 때,
        while queue :
            # 노드는 queue 리스트의 첫번째 값
            node = queue.pop(0)
            for i in range(n):
                # 지나가지 않았고, 컴퓨터 연결 선이 1일 때,
                if visited[i] == 0 and computers[node][i] == 1:
                    # 큐에 i 값 추가
                    queue.append(i)
                    # visited 리스트에 1 추가
                    visited[i] = 1
        answer += 1
    return answer
n = 3
visit = [[0] * n for _ in range(n)]
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(bfs(computers, n))