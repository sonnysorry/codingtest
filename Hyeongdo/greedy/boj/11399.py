#ATM
# 사실 재귀로 풀려했지만 런타임 에러가 떠서...
# 결국 그냥 dp 응용으로 for문으로 합쳐주면서 해주는 게 제일 나은듯 하다.
n = int(input())

arr = list(map(int, input().split()))

arr.sort()

arr_sum = [0] * n

arr_sum[0] = arr[0] 
for i in range(1, n):
    arr_sum[i] = arr_sum[i-1] + arr[i]

print(sum(arr_sum))