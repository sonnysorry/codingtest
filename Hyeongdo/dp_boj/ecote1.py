n = int(input())
food_list = list(map(int, input().split()))

d = [0] * 30001

d[0] = food_list[0]
d[1] = max(food_list[1], d[0])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + food_list[i])

print(d[n-1])
