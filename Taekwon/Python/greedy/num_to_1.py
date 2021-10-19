n, k = map(int, input().split())

count = 0

while True:
    if n == 1:
        break
    elif n % k == 0:
        n /= k
        count += 1
    elif n % k != 0:
        n -= 1
        count += 1
print(count)
