n = 6
times = [7, 10]
# 분할 정복 알고리즘이다.
# 최소와 최대를 (left, right 로 ) 대략적으로 잡고, 중간값을 잡아서
# left와 right의 간극을 줄여나가면서 mid 값을 answer로 만들면 된다.
# 이런 경우 순환형태로 나타내져서 재귀도 사용이 가능할 듯 하다.
def binary_search(times, n):
    # 우선 time을 sort해서 오름차순으로 만든다.
    times.sort()
    # 최소값만 쭉 돌리는 것이 제일 큰 수가 될 것이므로
    # 물론 제일 큰 것을 n 번 곱하는 게 제일 크겠지만, 허수이니 빼버린다.
    # right 값을 최소값의 곱으로 한다.
    right = n * min(times)
    # left는 가장 작은 값인 1로 한다.
    left = 1
    # 답인 answer값을 잡아준다.
    answer = 0
    # left와 right를 지속적으로 변경할 것이므로, while 문을 아래처럼 짜준다.
    # 궁극적으로는 같아져야 한다.
    while left <= right:
        # mid 값을 설정해준다 (중요 포인트)
        mid = (left + right) // 2
        # 임시 값을 변수로 설정 후 초기화한다.
        chk = 0
        # times의 값을 mid의 값으로 나눈 값으로 설정한다.
        # 이는 mid의 값이 각각 times의 값으로 나누어졌을 때,
        # 1인당 시간 내에 처리하는 사람의 수를 나타내준다.
        for line in times:
            chk += mid // line
            # n 값보다 처리 가능한 사람의 수가 크면
            # 어짜피 시간 내 처리 가능한 것이므로
            # 멈춘다.
            if chk >= n:
                break
        # 체크의 값이 n보다 작으면 미드 값이 작은 것이므로, left 값을 mid 보다 하나 키운다.
        if chk < n:
            left = mid +1
        # 체크의 값이 n보다 크면 미드 값이 큰 것 이므로, right 값을 mid 보다 하나 작게 한다.
        # answer 값을 mid로 갱신해준다.
        else:
            answer = mid
            right = mid - 1

    return answer

def rec_bin(time, n):
    time.sort()
    right = n * min(times)
    left = 1
    answer = 0
    mid = (left + right) // 2
    if left <= right:
        return mid
    else:
        rec_bin(time, )

print(binary_search(times, n))