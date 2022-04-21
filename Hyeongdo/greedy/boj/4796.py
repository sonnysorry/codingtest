# 캠핑
def countNum(l, p, v):
    answer = 0
    send_count = v//p
    last_count = v%p

    answer += send_count*l
    if last_count <= l:
        answer += last_count
    else:
        answer += l
    return answer

num = []
count = 0
while True:
    count += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    print("Case %d: %d"%(count, countNum(L, P, V)))
    
    

