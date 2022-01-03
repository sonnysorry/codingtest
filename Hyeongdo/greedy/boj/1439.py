# 뒤집기

s = input()

# 초기값과 달라질 때만 카운트 해주면 된다.
init = s[0]
temp = s[0]
count = 0
for i in range(1, len(s)):
    if temp != s[i]:
        temp = s[i]
        count += 1
        # 초기값과 동일할 때는 count를 빼준다.
        if temp == init:
            count -= 1

print(count)

