# 등차수열의 개수

n = int(input())

num_list = list(map(int, input().split(" ")))

count = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if num_list[j] - num_list[i] == num_list[k] - num_list[j]:
                count += 1

print(count)