number = "twofourthreeone"
num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_check_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

temp_list = []
for i in range(len(num_list)):
    temp_list.append(number.find(num_list[i]))
temp_dic = {}
for j in range(len(num_check_list)):
    temp_dic[str(num_check_list[j])] = temp_list[j]

sorted_temp = sorted(temp_dic.items(), key = lambda x: x[1])

answer = ""
for j in range(len(num_check_list)):
    if sorted_temp[j][1] != -1:
        answer += sorted_temp[j][0]
        
print(answer)