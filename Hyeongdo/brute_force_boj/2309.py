# 일곱난쟁이
# [boj-백준] Brute force 2309 일곱 난쟁이 - python
for _ in range(9):
    h_list.append(int(input()))
total = sum(h_list)
for i in range(9):
    for j in range(i+1, 9):
        sum_tot = total - h_list[i] - h_list[j]
        if sum_tot == 100:
            num1 = h_list[i]
            num2 = h_list[j]
            h_list.remove(num1)
            h_list.remove(num2)
            h_list.sort()
            for i in range(len(h_list)):
                print(h_list[i])
            break
    if len(h_list) < 9:
        break

