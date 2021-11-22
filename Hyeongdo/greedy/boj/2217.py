# 로프

n = int(input())
chk = []
for _ in range(n):
    chk.append(int(input()))

chk.sort(reverse=True)
max = chk[0]
for i in range(1, len(chk)):
    if max < chk[i]*(i+1):
        max = chk[i]*(i+1)

print(max)
