k = int(input())

def pelindrome(n):
    r = 0
    a = n
    while a > 0:
        r = r*10 + a%10
        a//=10
    return n == r

