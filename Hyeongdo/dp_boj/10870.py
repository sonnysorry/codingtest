# 피보나치 수 5

n = int(input())

def dp(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    return dp(x-1) + dp(x-2)
    
print(dp(n))