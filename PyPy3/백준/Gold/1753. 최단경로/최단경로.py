from collections import deque
import sys
input = sys.stdin.readline

#사람수와 파티수 입력
v, e = map(int, input().split())
start_pos = int(input())
lines = [{} for _ in range(v + 1)]
for _ in range(e):
    start, end, weight = map(int, input().split())
    if end in lines[start]:
        lines[start][end] = min(lines[start][end], weight)
    else:
        lines[start][end] = weight

lines = [list(s.items()) for s in lines]


visited = [False for _ in range(v + 1)]
visited[start_pos] = True
dist = [False for _ in range(v + 1)]
dist[start_pos] = 0
for line in lines[start_pos]:
    dest, weight = line
    dist[dest] = weight

while True:
    next_pos = -1
    min_weight = float("inf")
    for i in range(1, v + 1):
        if not visited[i] and dist[i] != False:
            if min_weight > dist[i]:
                next_pos = i
                min_weight = dist[i]


    if next_pos == -1:
        break

    visited[next_pos] = True
    for update_point, update_dist in lines[next_pos]:
        if not dist[update_point]:
            dist[update_point] = dist[next_pos] + update_dist
        else:
            dist[update_point] = min(dist[update_point], dist[next_pos] + update_dist)

dist[start_pos] = "0"

for i in dist[1:]:
    if i == False:
        print("INF")
    else:
        print(i)