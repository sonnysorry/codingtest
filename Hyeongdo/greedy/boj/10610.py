# 30
# 각 자리수의 합이 3이라는 것.
n = str(input())

num_list = []
for line in n:
    num_list.append(line)

# 정수로 형변환 하는 코드
num_list = list(map(int, num_list))

num_list = sorted(num_list, reverse=True)

if num_list[-1] != 0:
    print(-1)
elif sum(num_list) % 3 == 0 and num_list[-1] == 0:
    for i in range(len(num_list)):
        print(num_list[i], end = "")

