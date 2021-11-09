from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

li = list(map(int, input().split()))

result = 0

def count(array, value):
    right = bisect_right(array, value)
    left = bisect_left(array, value)
    return right - left

print(count(li, x))
