# 수리공 항승

n, l = map(int, input().split())

hole = list(map(int, input().split()))

hole_list = sorted(hole, reverse=True)

temp = hole_list[0]
for i in range(1, len(hole_list)):
    if l > temp - hole_list[i]:
        n -= 1
    else:
        temp = hole_list[i]

print(n)