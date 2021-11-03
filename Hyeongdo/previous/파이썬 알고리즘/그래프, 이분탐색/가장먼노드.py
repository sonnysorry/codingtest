from collections import deque
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    # 딕셔너리로 패스를 만든다.
    # 그래프를 딕셔너리로 해서 각 노드에 연결된 노를 파악하는 것이다.
    path = dict()
    for a, b in edge:
        path.setdefault(a, []).append(b)
        path.setdefault(b, []).append(a)
    # 노드의 초기 번호, 그리고 거리를 나타내는 값을 큐에 집어넣어
    # 2차원 배열을 만든다.
    queue = [[1, 0]]
    # -1 로 노드 거침을 파악한다.
    # 0으로 하면
    # n으로 하면 1~5으로 나와있어서  1~6 포함이 안됨.
    # 인덱스 에러 떠서 1추가 해준다.
    visited = [-1 for _ in range(n+1)]
    while queue:
        # 노드번호와 거리 값을 pop 한다.
        node, depth = queue.pop(0)
        # visited 안의 노드번호에 뎁스 값을 집어넣는다.
        visited[node] = depth
        # 각각의 노드에서 연결 path의 값을 체크한다.
        for i in path[node]:
            # 아직 그 노드를 거치지 않았으면,된
            # 즉, 다시 되돌아가지 않으면
            if visited[i] == -1:
                # 0으로 바꿔주고,
                visited[i] = 0
                # 거리를 하나 이동해준다.
                # 그리고 앞에서부터 pop하는 과정을 거쳐서 이동시킨다.
                queue.append([i, depth + 1])
        depth += 1
    return visited.count(max(visited))

print(solution(n, edge))
