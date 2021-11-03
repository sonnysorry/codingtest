#백트래킹으로 먼저 짜기
pattern = ( (1, 0, 0) , (0 , 1, 0), (0, 0, 1), (1, 0, 1) )
def solve(cur, last, n, sum, tbl):
    max = sum
    for p in pattern:
        t = last[0] * p[0] + last[1] * p[1] + last[2] * p[2]
        if t != 0: continue
        nsum = sum + tbl[0][cur]*p[0] + tbl[1][cur] * p[1] + tbl[2][cur] * p[2]
        r = solve(cur+1, p, n, nsum, tbl)
        if max < r : max = r
    return max

n = int(input())
tbl = []
for _ in range(3):
    row = tuple(map(int, input().split()))
    tbl.append(row)
print(solve(0, 0, n, 0, tbl))

