import heapq
import sys
import time

input = sys.stdin.readline

n, m, x = map(int, input().split())
x -= 1

forward_graph = [[] for _ in range(n)]
backward_graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    forward_graph[a].append([b, w])
    backward_graph[b].append([a, w])


# print(forward_graph)
# print(backward_graph)


def dijkstra(graph, start):
    dist = [float("INF") for _ in range(n)]
    q = []
    heapq.heappush(q, [0, start])

    while q:
        curr_dist, curr_point = heapq.heappop(q)

        if dist[curr_point] < curr_dist:
            continue

        dist[curr_point] = curr_dist

        for next_point, next_dist in graph[curr_point]:
            if next_dist + curr_dist < dist[next_point]:
                heapq.heappush(q, [next_dist + curr_dist, next_point])

    return dist


forward_table = dijkstra(forward_graph, x)
backward_table = dijkstra(backward_graph, x)
ans = 0
for i in range(n):
    ans = max(ans, forward_table[i] + backward_table[i])

print(ans)