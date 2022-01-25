# 상하좌우 답안 
# [이코테 강좌] Brute force 1번 상하 좌우 - python 
n = int(input())
# 초기값 설정
x, y = 1, 1
plans = input().split()

# 아래 MOVE TYPE에 따른 이동 방향 체크
# x좌표와 y 좌표 문자를 각각 같은 인덱스로 설정해주는 방식이다.
# 체크해서 활용하자.
dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이중 포문 사용해서 이렇게 돌려서 타입을 체크하는 방식이다.
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

print(x, y)
