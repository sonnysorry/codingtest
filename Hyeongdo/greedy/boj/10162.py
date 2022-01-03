# 전자레인지

T = int(input())

button = [300, 60, 10]
count = [0, 0, 0]

for i in range(len(button)):
    if T >= button[i]:
        count[i] += T // button[i]
        T %= button[i]

if T != 0:
    print(-1)
else:
    for j in range(0, len(count)):
        print(count[j], end = " ")
