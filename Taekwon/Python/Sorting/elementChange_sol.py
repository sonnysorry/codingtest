# 배열의 인덱스가 10만개까지 늘어날 수 있으므로 O(N제곱)의 알고리즘 성능으로는 안된다. 그래서 정렬을 직접 구현하라는 말이 없으면 무조건 sort() 함수 사용할 것.
n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # 배열 A는 오름차순 정렬 수행
B.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        # 두 원소를 교체
        A[i], B[i] = B[i], A[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(A)) # 배열 A의 모든 원소의 합을 출력
