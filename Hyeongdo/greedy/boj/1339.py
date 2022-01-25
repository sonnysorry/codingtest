# 단어수학

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(input())

num_dict = {"*": 0}

# 요소 길이 순 정렬
num_list.sort(key=len, reverse=True)

chk = 9

for i in range(n):
    if len(num_list[i]) < len(num_list[0]):
        b = (len(num_list[0]) - len(num_list[i])) * "*" + num_list[i] 
        num_list[i] = b

for k in range(len(num_list[0])):
    for j in range(len(num_list)):
        if num_list[j][k] not in num_dict:
            num_dict[num_list[j][k]] = chk
            chk -= 1
        else:
            continue

answer = []
for p in range(len(num_list)):
    temp = ""
    for t in range(len(num_list[0])):
        temp += str(num_dict[num_list[p][t]])
    answer.append(int(temp))
    
print(sum(answer)) 

