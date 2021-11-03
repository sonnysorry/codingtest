import heapq
import time
K = 7
scoville = [1,2,3,9,10,12]
t = time.time()

heapq.heapify(scoville)
count = 0
while scoville[0] < K:
    try:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + b*2
        heapq.heappush(scoville, c)
    except IndexError:
        # 런타임에러 발생으로 인해 index 에러 뜨면 -1 return 함.
        # 이 경우 길이가 매우 짧을 때 이렇게 됨.
        return -1
    count += 1
print(count)
t = (time.time() - t) *1000

print("elapsed time : %0.fms" %t)