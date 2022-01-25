#왕실의 나이트

n = input()
x = ord(n[0]) - 96
y = n[1]
# 꿀팁!
# x, y 좌표를 각각 표현해주고 경우의 수를 표현해준다
# 각각 좌표는 인덱스 값이며 각 인덱스 별로 나눠서 체크한다.
move_x = [1, 1, -1, -1, 2, 2, -2, -2]
move_y = [2, -2, 2, -2, 1, -1, 1, -1]

count = 0
for i in range(8):
    nx = int(x) + move_x[i]
    ny = int(y) + move_y[i]
    count += 1
    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        count -= 1

print(count)