# 문자열 재정렬

n = input()
temp = []
char_list = []
for i in range(len(n)):
    if int(ord(n[i])) < int(ord("A")):
        temp.append(int(n[i]))
    else:
        char_list.append(n[i])

answer = sorted(char_list)
answer_2 = str(sum(temp))
answer.append(answer_2)
for j in range(len(answer)):
    print(answer[j], end="")

