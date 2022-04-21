# 보석 도둑

from re import L


n, k = map(int, input().split())

jewel_list = []
sac_list = []
check_list = [0] * 100001
for _ in range(n):
    jewel_list.append(list(map(int, input().split())))

for _ in range(k):
    sac_list.append(int(input()))

jewel_list = sorted(jewel_list, key=lambda x:x[1], reverse = True)
sac_list = sorted(sac_list)
answer = 0
for i in range(k):
    for j in range(n):
        if sac_list[i] >= jewel_list[j][0] and check_list[j] == 0:
            answer += jewel_list[j][1]
            check_list[j] = 1
            break

print(answer)


