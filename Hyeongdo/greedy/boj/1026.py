#보물
# A[i]*B[i] 가 최저값이 되어야하므로 하나는 오름, 하나는 내림차순 해준다.

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A.sort(reverse=True)

answer = 0
for i in range(n):
    answer += A[i]*B[i]

print(answer)