# 셀프 넘버
# [boj-백준] Brute force 4673 셀프 넘버 - python

chk = []
for i in range(1, 10000):
    num_list = list(map(int, str(i)))
    sum_num_list = sum(num_list)
    sum_all = i + sum_num_list
    chk.append(sum_all)

for i in range(1, 10001):
    if not i in chk:
        print(i)