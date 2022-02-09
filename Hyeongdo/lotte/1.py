 # "onetwothreefour"
 # 위의 문자열 주어졌을 때 문자열로 뽑아서 오기

number = "onetwothreefour"
num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_check_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sep_num = ""
temp_list = []

for i in range(len(number)):
    sep_num += number[i]
    if sep_num in num_list:
        temp_list.append(sep_num)
        sep_num = ""
answer = ""
for line in temp_list:
    for j in range(len(num_list)):
        if num_list[j] == line:
            answer += str(num_check_list[j])
print(answer)