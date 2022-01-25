# 이코테 강좌 상하좌우

n = int(input())
move_list = list(map(str, input().split(" ")))

init = [1, 1]
direction = {"R" : [0, 1], "L" : [0, -1], "U" : [-1, 0], "D" : [1, 0]}

for line in move_list:  
    init[0] += direction[line][0]
    init[1] += direction[line][1]
    if init[0] < 1 or init[0] > n or init[1] < 1 or init[1] > n:
        init[0] -= direction[line][0] 
        init[1] -= direction[line][1]

print(init[0], init[1], end = ' ')
