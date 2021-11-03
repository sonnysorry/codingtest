n = int(input())
s1 = 1
nodiv = 1
if (n % 2 == 0):
    s = 1
    while(n%2 == 0):
        n /= 2
        s = s*2 + 1
    s1 *= s
i = 3
while i*i <= n:
    if n%i != 0: continue
    s = 1
    while n%i == 0:
        s = s*i + 1
        n //= i
    s1 *= s
    i += 2
if n > 1: s1 *=  n+1
print(s1)