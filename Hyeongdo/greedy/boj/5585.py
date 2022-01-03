#거스름돈

n = 1000 - int(input())

num = [500, 100, 50, 10, 5, 1]

count = 0
for line in num:
    chk = 0 
    if line <= n:
        count += n // line
        n %= line

print(count)