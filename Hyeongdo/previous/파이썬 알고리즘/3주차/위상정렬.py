import queue
n = int(input())
vert = [0] * (n+1)
k = int(input())
adjlist = [[] for _ in range(k)]

for i in range(k):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    vert[b] += 1

# 큐 만들기
que = queue.Queue()

# vert[k] = 0 찾기, k를 큐에 넣
for i in range(1, n+1):
    if vert[i] == 0:
        que.put(i)
vertCount = 0
s = ""
while not que.empty():
    r = que.get()
    s += str(r) + " "
    vertCount += 1
    for k in adjlist[r]:
        vert[k] -= 1
        if vert[k] == 0: que.put(k)

if vertCount != n: print("Error")
else: print(s)
