# 저울
# 수리적 원리의 문제였다....
# 결국엔 더하기 해서 더 큰 수가 타겟으로 나오면 안되는 원리.


n = int(input())
num_list = list(map(int, input().split(" ")))

s_num_list = sorted(num_list)

target = 1
for i in s_num_list:
    if target < i :
        break
    target += i

print(target)