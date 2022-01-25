#거스름돈

n = 1000 - int(input())

num = [500, 100, 50, 10, 5, 1]

count = 0
for line in num:
    chk = 0 
    if line <= n:
        # 나눈 값을 넣어주고
        count += n // line
        # 남은 값은 어짜피 나머지이니 나머지 개념을 이용하면 되는 문제이다.
        n %= line

print(count)