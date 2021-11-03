s, k = map(int, input().split())

n = s//k
if s % k == 0:
    print(pow(n, k))

else:
    answer = 1
    while k != 0:
        if s % k != 0:
            answer *= n
            s -= n
            k -= 1
        else:
            answer = answer * pow(s//k, k)
            k = 0
            s = 0
    print(answer)