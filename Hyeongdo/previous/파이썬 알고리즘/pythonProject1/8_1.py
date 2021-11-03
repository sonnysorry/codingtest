def findroot(set, x):
    if set[x] == x: return x
    set[x] = findroot(set, set[x])
    return set[x]

n = int(input())
k = int(input())

edges = []
for _ in range(k):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

edges.sort(key = lambda x : x[2])

set = [i for i in range(n+1)]
complete = 0