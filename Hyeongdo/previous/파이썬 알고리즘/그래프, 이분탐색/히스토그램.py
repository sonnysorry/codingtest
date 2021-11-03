histo = [3,2,3,4,2,3,4]
n = 6
def dac(histo, a, b):
    # 가운데 만나는 지
    if a == b : return histo[a]
    # mid
    c = (a+b)// 2
    # max 값 초기화 (왼 - 중간)
    max = dac(histo, a, c)
    # right 값 초기화 (중간 - 오)
    r = dac(histo, c+1, b)
    if max < r: max = r
    # min 값 초기화 (최소 높이)
    min = histo[c]
    # 최소높이 구하는 알고리즘
    if min > histo[c+1]: min = histo[c+1]
    # 왼쪽으로 한칸, 오른쪽으로 두칸 간 상태에서 시작한다.
    # 시작 점도 잡아준다.
    i = c-1
    j = c+2
    w = 2
    # 최소 높이 * 길이 가 max 보다 크면 max 바꿈
    if max < min * w : max = min*w
    while i >= a and j <= b:
        if histo[i] > histo[j]:
            if min > histo[i] : min = histo[i]
            i -= 1
        else:
            if min > histo[j] : min = histo[j]
            j += 1
        w += 1
        if max < min * w : max = min * w
    # 끝나고 왼쪽 남았을 때,
    while i >= a:
        if min > histo[i] : min = histo[i]
        i -= 1
        w += 1
        if max < min * w: max  = min * w
    # 끝나고 오른 쪽 남았을 때
    while j <= b:
        if min > histo[j] : min = histo[j]
        j += 1
        w += 1
        if max < min * w : max = min * w
    return max
print(dac(histo, 0, n-1))