def dfs(tickets):
    visit = [0 for _ in range(len(tickets))]
    stack = ["ICN"]

    if depth == len(tickets):
        return stack
    stack.append(root)
    new_list = []
    new_list.append(root)
    while stack:
        node = stack.pop()
        for i in range(len(tickets)):
            if(tickets[i][0] == node and visit[i] == 0):
                new_list.append(node)
                visit[i] = 1
    return new_list

import queue
def solution(tickets):
    tickets.sort(key = lambda x:x[1])
    que = queue.Queue()
    visited = [0 for _ in range(len(tickets))]
    new_list = []
    que.put("ICN")
    while que:
        node = que.get()
        new_list.append(node)
        for i in range(len(tickets)):
            if tickets[i][0] == node and visited[i] == 0:
                que.put(tickets[i][1])
                visited[i] = 1
                break
        print(visited)
    return new_list

def bfs(tickets):
    tickets.sort(key = lambda x:x[1])
    stack = []
    visited = [0 for _ in range(len(tickets))]
    stack.append("ICN")
    while sum(visited) < len(tickets):
        node = stack[-1]
        for i in range(len(tickets)):
            if tickets[i][0] == node and visited[i] == 0:
                stack.append(tickets[i][1])
                visited[i] = 1
                break
    return stack
#visited = [1, 1, 1, 1, 1]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets.sort(key = lambda x:x[1])
print(tickets)
import time
t = time.time()
print(solution(tickets))
t = (time.time() - t) *1000
print("elapsed time : %.0fms" %t)
