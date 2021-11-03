def uclid(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

n = int(input())
A = 1
for i in range(n):
    p = int(input())
    A = A * p
m = int(input())
B = 1
for j in range(m):
    t = int(input())
    B = B * t
print(uclid(A,B))

