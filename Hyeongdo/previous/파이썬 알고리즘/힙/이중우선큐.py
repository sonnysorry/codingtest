import heapq
operations = ["I 7","I 5","I -5","D -1"]
heap = []

for i in operations:
    x, y = i.split(" ")
    if x == "I":
        heapq.heappush(heap, int(y))
    else:
        if x == "D" and y == "1":
            heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
        elif x == "D" and y == "-1":
            heapq.heappop(heap)

if len(heap) == 0:
    print([0, 0])
else:
    print([heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]])
