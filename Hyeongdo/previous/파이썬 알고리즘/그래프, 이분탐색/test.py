histo = [3,2,3,4,2,3,4]
n = 6
def dac(histo, a, b):
    # 가운데 만나는 지점
    if a == b : return histo[a]
    # mid
    c = (a+b) // 2
    max = dac(histo, a, c)
    r = dac(histo, c+1, b)
    if max < r: max = r
    min = histo[c]
    if min > histo[c+1]: min = histo[c+1]
    i = c-1
    j = c+2
    w = 2
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

    while i >= a:
        if min > histo[i] : min = histo[i]
        i -= 1
        w += 1
        if max < min * w: max  = min * w

    while j <= b:
        if min > histo[j] : min = histo[j]
        j += 1
        w += 1
        if max < min * w : max = min * w
    return max
print(dac(histo, 0, n-1))