#1이 될 때 까지

n, k = map(int, input().split())

count = 0 
while True:
    if n == 1:
        break
    elif n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)