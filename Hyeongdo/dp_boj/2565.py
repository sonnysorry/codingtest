n = int(input())

num_list = []
for _ in range(n):
    num_list.append(list(map(int, input().split())))

num_list.sort(key=lambda x:x[0])
