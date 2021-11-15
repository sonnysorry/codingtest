# 거스름돈

chart = [500, 100, 50, 10]

n = int(input("거슬러 줄 돈 : "))

count = 0
for line in chart:
    count += n // line
    n %= line

print(count)