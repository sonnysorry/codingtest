import queue
import math

INF = 10000000000
# A* 알고리즘에서 거리를 측정하는 함수
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2)

n = int(input())
adjlist = [[] for _ in range(n+1)]
v = [(0, 0)]
for i in range(n):
    a, b = map(int, input().split())
    v.append((a, b))
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    adjlist[a].append((b, distance(v[a], v[b])))

start, end = map(int, input().split())

visited = [False] * (n+1)
values = [INF] * (n+1)
pq = queue.PriorityQueue()
values[start] = 0
pq.put((0, start))

while not pq.empty():
    s, r = pq.get()
    if r == end: break
    if visited[r]: continue
    visited[r] = True
    for c, w in adjlist[r]:
        t = values[r] + w
        if values[c] > t:
            values[c] = t
            pq.put((t + distance(v[r], v[c]), c))

print(values[end])
