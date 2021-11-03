n = int(input())
v = list(map(int, input().split()))

max = v[0]
min = v[0]
for i in range(n):
    if(v[i] > max):
        max = v[i]
    if(v[i] < min):
        min = v[i]
print("%d %d" % (min, max))

