INF = 100000000
n = int(input())

# 거리를 저장할 nxn 배열 선언
# 모든 배열 값을 무한대로 설
d = [[INF]*(n+1) for _ in range(n+1)]

# 경로를 저장하기 위한 n x n 배열 선언
next = [[k for k in range(n+1) ] for _ in range(n+1) ]

# 대각 배열 값을 0으로 초기화정
# 대각행렬만 0
for i in range(1, n+1): d[i][i] = 0
# k개의 간선을 받음
# 각각에 w 값(가중치)을 받음
# 중간노드 하나도 방문 안했을 떄의 초기 상태
k = int(input())
for _ in range(k):
    a, b, w = map(int, input().split())
    d[a][b] = w

# Floyd Warshall Algorithm
for m in range(1, n+1):
    for u in range(1, n+1):
        for v in range(1, n+1):
            if d[u][m] == INF or d[m][v] == INF: continue
            if d[u][v] > d[u][m] + d[m][v]:
                d[u][v] = d[u][m] + d[m][v]
                next[u][v] = next[u][m]

# 순환 노드에서 음의 사이클이 있는 지 여부를 검사하는 부분이다.
# 대각성분을 보면 된다.
isMinusCycle = False
for i in range(1, n+1):
    if d[i][i] < 0 :
        isMinusCycle = True
        break
if isMinusCycle:
    print("Minus Cycle detected");
    quit()

#print
for u in range(1, n+1):
    s = ""
    for v in range(1, n+1):
        if d[u][v] == INF: s += "INF"
        else: s += "%3d " %d[u][v]
    print(s)

#print path
