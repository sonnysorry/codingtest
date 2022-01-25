#모의고사

def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        a = i % len(first)
        b = i % len(second)
        c = i % len(third)
        if int(first[a]) == int(answers[i]):
            count[0] += 1
        if int(second[b]) == int(answers[i]):
            count[1] += 1
        if int(third[c]) == int(answers[i]):
            count[2] += 1
    max_count = max(count)
    for j in range(len(count)):
        if max_count == count[j]:
            answer.append(j+1)       
    return answer

answers = [1,2,3,4,5]
print(solution(answers))