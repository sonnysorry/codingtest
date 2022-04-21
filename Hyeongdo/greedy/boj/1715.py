# 카드 정렬하기


n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

temp = num_list[0] + num_list[1]
for i in range(2, len(num_list)):
    temp *= 2
    temp += num_list[i]
    

print(temp)