n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

sorted_A = quick_sort(A)
sorted_B = quick_sort(B)

count = len(B) - 1

# 이 부분 잘못 푼게, 배열 A와 B의 값을 비교해가면서 했어야 했는데, 무작정 A와 B의 배열 인덱스에 담긴 값을 바꿔버려서 문제가 될 수 있었다.
for i in range(k):
    sorted_A[i], sorted_B[count] = sorted_B[count], sorted_A[i]
    count -= 1

result = 0
for i in range(len(sorted_A)):
    result += sorted_A[i]

print(result)
