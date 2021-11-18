#신입 사원
# 문제가 좀 괴랄했음.
# 일반 input으로 입력하면 시간초과가 뜬다...
# sys 가지고 readline 써서 입력 받아야하는데, 이 경우 코테에서 사용이 제한되므로.. 좀 애매한 문제.
import sys

t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    test = []
    for _ in range(n):
        Paper, Interview = map(int,sys.stdin.readline().split())
        test.append([Paper, Interview])

    # 우선 행으로 sorting 한다.

    test.sort()
    # 소팅한 값에서 처음 값은 무조건 들어가니 max로 하고 count 높여준다.
    count = 1
    max = test[0][1]
    # for 문 돌면서 max 값보다 작으면 count 해주고 max값을 바꿔준다.
    for i in range(n):
        if max > test[i][1]:
            count += 1
            max = test[i][1]
    print(count)