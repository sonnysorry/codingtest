citations = [3, 0, 6, 1, 5, 6, 6]
citations.sort(reverse = True)
print(citations)
answer =  len(citations)
for idx, line in enumerate(citations):
    if line >= answer and len(citations[idx:]) >= answer:
        print answer
    else:
        answer -= 1;
        continue

def solution(citations):
    citations.sort(reverse = True)
    answer =  0
    for idx, line in enumerate(citations):
        if idx + 1 >= line:
            answer = line
            break;
        elif len(citations) <= line:
            answer = len(citations)
    return answer