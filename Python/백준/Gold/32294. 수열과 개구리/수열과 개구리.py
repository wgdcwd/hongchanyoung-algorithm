import sys
import heapq

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    if a[i] >= min(i, n - i + 1):
        graph[0].append([i, 0])
    else:
        graph[i - a[i]].append([i, b[i - a[i]]])
        graph[i + a[i]].append([i, b[i + a[i]]])




dist = [float("INF") for _ in range(n + 1)]
q = []
for i in graph[0]:
    heapq.heappush(q, [i[1], i[0]])


while q:
    curr_dist, curr_pos = heapq.heappop(q)

    if dist[curr_pos] <= curr_dist:
        continue
    dist[curr_pos] = curr_dist

    for next_pos, next_dist in graph[curr_pos]:
        heapq.heappush(q, [curr_dist + next_dist, next_pos])


for i in range(1, n + 1):
    print(dist[i] + b[i], end=" ")