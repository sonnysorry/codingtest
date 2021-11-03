import time
t = time.time()

n = int(input())
sum = 0
for i in range(1, n+1):
    if n % i == 0 :
        sum += i
print(sum)
t = (time.time() - t) *1000
print("elapsed time : %.0fms" %t)