from math import factorial
def get_factorial_num(range_from, range_to):
    result_sum = 0
    for num in range(range_from, range_to):
        list_num = list(str(num))
        sum = 0
        for i in list_num :
            sum = sum + factorial(int(i))
            if num == sum :
                result_sum += num
    return result_sum

print(get_factorial_num(10, 100000))

