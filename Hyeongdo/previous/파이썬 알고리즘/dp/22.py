def solution(n, number):
    answer = 0
    d = [[] for i in range(9)]  # n을 사용하는 개수가 인덱스가 됨. 인덱스가 1이면 n을 한번 사용하는 경우, 2면 n을 두번 사용하는 경우,,
    d[1].append(n)  # n을 한번만 사용하는 경우는, n 그 자체일 때 뿐이므로 리스트에 추가.

    for i in range(2, 9):
        # 숫자가 5면, 숫자를 2개 사용하는 경우에는 55, 3개 사용하는 경우에는 555
        # ... 8개 사용하는 경우에는 55555555가 나올 수 있으므로 리스트에 추가.
        num = int(str(n) * i)
        d[i].append(num)

    for i in range(2, 9):  # i는 사용하는 n의 개수
        for j in range(1, i):
            # 사용하는 n의 개수가 i개이면, 사용하는 n의 개수가 1인 것과 (i-1)인 것, 2인것과 (i-2)인 것
            # ..... i-1개인 것과 1개인 것의 조합들로 만들 수 있음.
            # 예를 들어, 2번 사용하면 1번 사용하는 경우와 1번 사용하는 경우의 조합으로,
            # 3번 사용하면 1번 2번 / 2번 1번 의 조합으로, 4번 사용하면 1 3/ 2 2/ 3 1 의 조합으로 ,, 변수를 추가해야함.
            # 이 숫자들을 잘 살펴보면 j는 1개만 사용하는 경우부터 i-1번 사용하는 경우까지,
            for z in range(len(d[j])):
                # 위의 조합들로 계산을 하기 위해서는, j번 사용하는 경우에 들어있는 리스트 안에 들은 수들과, i-j번 사용하는 경우의 리스트 안의 수들을 모두 조합해주어야함.
                # 따라서 인덱스가 0인 것부터, j번 사용하는 경우의 리스트의 길이 -1 까지의 원소들을 모두 살펴봐야함.
                for t in range(len(d[i - j])):  # j번 사용하는 경우는, i-j번 사용하는 경우와 조합해야 하므로 ,,
                    num1 = d[j][z] + d[i - j][t]  # 조합 1) 덧셈
                    num2 = d[j][z] * d[i - j][t]  # 조합 2 ) 곱셈
                    num3 = d[j][z] - d[i - j][t]  # 조합 3) 뺄셈
                    if d[i - j][t] != 0 and d[j][z] % d[i - j][
                        t] == 0:  # 조합 4) 나눗셈 : 0으로는 나눌 수 없으므로 나누는 수가 0이면 안됨. 또한 나누어 떨어지는 경우여야함.
                        num4 = d[j][z] // d[i - j][t]

                    if num1 not in d[i]:
                        d[i].append(num1)
                    if num2 not in d[i]:
                        d[i].append(num2)
                    if num3 not in d[i]:
                        d[i].append(num3)
                    if num4 not in d[i]:
                        d[i].append(num4)

    for i in range(1, 9):
        if number in d[i]:
            answer = i
            break
        else:
            answer = -1

    return answer