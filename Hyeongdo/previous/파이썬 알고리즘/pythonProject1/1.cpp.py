n, k = map(int, input().split())
sum = 0
for i in range(k, n+1, k):
    if i % k == 0:
        sum += i
print(sum)