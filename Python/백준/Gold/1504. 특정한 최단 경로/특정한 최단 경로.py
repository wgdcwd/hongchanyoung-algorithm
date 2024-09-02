import heapq
from collections import deque
import sys

input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, weight = map(int, input().split())
    graph[a].append([b, weight])
    graph[b].append([a, weight])

a, b = map(int, input().split())


def cal(start):
    dist = [float("INF") for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    q = []
    heapq.heappush(q, [0, start])

    while q:
        curr_dist, curr_point = heapq.heappop(q)

        if curr_dist >= dist[curr_point]:
            continue

        dist[curr_point] = curr_dist

        for next_point, next_dist in graph[curr_point]:
            heapq.heappush(q, [curr_dist + next_dist, next_point])

    return dist


start_table = cal(1)
a_table = cal(a)
b_table = cal(b)
route_a = start_table[a] + a_table[b] + b_table[n]
route_b = start_table[b] + b_table[a] + a_table[n]
ans = min(route_a, route_b)
if ans == float("INF"):
    ans = -1
print(ans)