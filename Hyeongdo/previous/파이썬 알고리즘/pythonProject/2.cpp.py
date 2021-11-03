n = 5
reserve = [1, 3, 5]
lost = [2, 4]

count = n;
count = count - len(lost);
for k in range(len(lost)):
    if (lost[k] + 1) or (lost[k] - 1) in reserve:
        count += 1
        reserve.remove(lost[k])
print(count)


