import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


bus = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    bus[start].append([end, weight])

start, end = map(int, input().split())

dist = [[float("inf"), []] for _ in range(n + 1)]
dist[start] = [0, -1]
q = []
for dest, w in bus[start]:
    heapq.heappush(q, [w, dest, start])

while q:
    curr_weight, curr_pos, prev_pos = heapq.heappop(q)
    if curr_weight > dist[curr_pos][0]:
        continue
    dist[curr_pos] = [curr_weight, prev_pos]

    for next_pos, next_weight in bus[curr_pos]:
        if curr_weight + next_weight < dist[next_pos][0]:
            heapq.heappush(q, [curr_weight + next_weight, next_pos, curr_pos])
    bus[curr_pos] = []
print(dist[end][0])
stk = [end]
while True:
    if dist[stk[-1]][1] == -1:
        break
    stk.append(dist[stk[-1]][1])
print(len(stk))
print(*stk[::-1])