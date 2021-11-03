k = int(input())

def rec(n):
    if n < 10 :
        return n
    else:
        return n % 10 + rec(n // 10)
while True:
    a = rec(k)
    if a < 10:
        print(a)
        break;
    else:
        a = rec(a)