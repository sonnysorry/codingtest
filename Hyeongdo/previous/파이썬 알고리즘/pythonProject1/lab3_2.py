
def hanoi(n, k):
    if k <= 0 : return k
    if n == 0 : return k
    k  = hanoi(n-1, k)
    k -= 1
    if k == 0:
        print(n)
        return 0
    k = hanoi(n-1, k)
    return k
k = int(input())
hanoi(32, k)