n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
result = 0
count = 0

for _ in range(m):
    if count == k:
        result += data[n-2]
        count = 0
    else:
        result += data[n-1]
        count += 1


print(result)
