# 재귀는 큰 수를 넣으면 상당히 오래걸린다.
# 재귀는 O(2^n) 알고리즘 이다.
def dp(x):
    # 재귀함수의 종료 조건.
    if (x == 1 or x == 2) : return 1
    return dp(x-1) + dp(x-2)

# 다음은 한번 구한 값은 메모이제이션을 이용해서 반환하게 만들것이다.
d = [0 for _ in range(100)]
def dp1(n):
    if (n == 1 or n == 2) : return 1
    if (d[n] != 0) : return d[n]
    d[n] = dp1(n-1) + dp1(n-2)
    return d[n]

print(dp1(30))
