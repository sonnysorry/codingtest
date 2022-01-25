# 분해합
# 브루트포스의 정석
# 각각 1부터 쭉 해주는 것에 for문을 쓰는데 인색하지 말자.
# 정말 앞에서부터 하나하나 쓰는 것을 중심으로 가야한다.
# [boj-백준] Brute force 2231 분해 합 - python

n = int(input())

for i in range(1, n+1):
    a = list(map(int, str(i)))
    sum_sep = sum(a)
    sum_all = i + sum_sep
    if sum_all == n:
        print(i)
        break
    if i == n:
        print(0)