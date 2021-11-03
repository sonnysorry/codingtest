answers = [1,2,3,4,5]
first = [1, 2, 3, 4, 5];
second = [2, 1, 2, 3, 2, 4, 2, 5];
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

chk = [0, 0, 0]
for i in range(len(answers)):
    if (first[i % len(first)] == answers[i]):
        chk[0] += 1;
    if (second[i % len(second)] == answers[i]):
        chk[1] += 1;
    if (third[i % len(third)] == answers[i]):
        chk[2] += 1;

answer = []
for idx, k in enumerate(chk):
    if k == max(chk):
        answer.append(idx + 1)
print(answer)