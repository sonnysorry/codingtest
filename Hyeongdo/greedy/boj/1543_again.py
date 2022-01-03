# 문서 검색

a = input()
b = input()

c = len(a)
chk = 0
count = 0
while chk <= c :
    okay = 0
    for i in range(len(b)):
        if b[i] == a[chk]:
            chk += 1
            okay += 1
    if okay == 3:
        count += 1        

print(count)