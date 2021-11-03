answer = []
brown = 10
yellow = 2
for i in range(1, int(yellow ** 0.5) + 1):
    if yellow % i == 0:
        j = yellow // i
        if 2 * (i + j) + 4 == brown:
            answer = [j + 2, i + 2]
print(answer)
print(int(yellow ** 0.5))