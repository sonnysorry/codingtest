#신입 사원
import sys

t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    test = []
    for _ in range(n):
        Paper, Interview = map(int,sys.stdin.readline().split())
        test.append([Paper, Interview])

    test.sort()
    count = 1
    max = test[0][1]
    for i in range(n):
        if max > test[i][1]:
            count += 1
            max = test[i][1]
    print(count)