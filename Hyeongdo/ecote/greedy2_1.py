#1이 될때까지 더 좋은 풀이

n, k = map(int, input().split())

result = 0

while True:
    # N이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    result += (n-target)
    n = target
    # n이 k보다 작을 때 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)