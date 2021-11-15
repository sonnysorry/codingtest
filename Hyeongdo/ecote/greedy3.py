# 곱하기 혹은 더하기 

n = str(input())

result = 0
for i in range(0, len(n)):
    if int(n[i]) <= 1 or result <= 0:
        result += int(n[i])
    else:
        result *= int(n[i])

print(result)