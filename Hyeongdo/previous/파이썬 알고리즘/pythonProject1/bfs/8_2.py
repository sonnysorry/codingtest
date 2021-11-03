import queue
n = int(input())
adjMat = [[0]*(n+1) for _ in range(n+2)]
k = int(input())
for _ in range(k):
    a, b, w = map(int, input().split())
    #정
    adjMat[a][b] = w
start = int(input())
#prim algorithm
visited = [False]*(n+1)
values = [1000000]*(n+1)
queue = queue.PriorityQueue()
values[start] = 0
queue.put((0, start))
while not queue.empty():
    s, r = queue.get()
    if visited[r]: continue
    print("vertex : %d , value = %d" %(r,s))
    visited[r]  =True
    for i in range(1, n+1):
        if adjMat[r][i] != 0 and not visited[i] and values[i] > adjMat[r][i]:
            #프림 손 안대고 바꿀 수 있음. 그냥 r -> t, values[i] -> t 로 바꿔주면 됨.
            values[i] = adjMat[r][i]
            queue.put((values[i], i))
    for i in range(1, n+1):
        print(values[i])