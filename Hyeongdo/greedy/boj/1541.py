#잃어버린 괄호

line = input()
# - 중심으로 스트링 나누고
line_list = line.split("-")


temp = []
#나눈 리스트에서 + 중심으로 스트링 나눠서 합치고 temp 리스트에 넣는다.
for check in line_list:
    let = check.split("+")
    int_let = list(map(int, let))
    temp.append(sum(int_let))

# 처음건 temp의 첫번째 수 
first = temp[0] 
# 그 외 나머지 수
sec = 0
for i in range(1,len(temp)):
    sec += temp[i]
#빼기
print(first - sec)