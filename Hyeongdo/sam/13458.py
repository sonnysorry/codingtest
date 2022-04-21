"""
시험장 n개
i 시험장 응시자 Ai명
총감독 감시 : B명 / 1명
부감독 감시 : C명 / 여러명 가능
"""

n = int(input())
num_list = list(map(int,input().split()))
b, c = map(int,input().split())
answer = 0
for i in range(len(num_list)):
    stu_num = num_list[i]
    stu_num -= b
    answer += 1
    if stu_num > 0:
        answer += stu_num // c
        if stu_num % c > 0:
            answer += 1
print(answer)