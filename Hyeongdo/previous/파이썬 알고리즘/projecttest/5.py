n = int(input())
DVD = []
for i in range(1, n+1):
    DVD.append(i)
m = int(input())
for _ in range(m):
    chk = int(input())
    a = DVD.index(chk)
    print(a+1)
    del DVD[a]
    DVD.insert(0, chk)