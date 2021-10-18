# 못 푼 문제

n = input()
result = int(n[0])

for i in n:
    if i == n[0]:
        continue
    elif int(i) >= 2:
        result *= int(i)
    else:
        result += int(i)

print(result)
