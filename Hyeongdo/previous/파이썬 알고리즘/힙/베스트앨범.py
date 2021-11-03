import heapq

genres = [classic, pop, classic, classic, pop]
plays = [500, 600, 150, 800, 2500]

heapq.heapify(genres)
import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(heap, (t, s))
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += (time - start)
        else:
            time += 1
    return answer//len(jobs)

