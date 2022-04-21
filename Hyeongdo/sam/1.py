# 구슬 탈출 2

from collections import deque

n, m = map(int, input().split())
num_list =[]
for _ in range(n):
    num_list.append(list(map(int, input().split())))
memo = []

def bfs():
    while q:
