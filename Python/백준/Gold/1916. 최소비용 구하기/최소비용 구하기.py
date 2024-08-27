import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

shortest = [n * 100000 for _ in range(n + 1)]
lines = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


for _ in range(m):
    start, end, weight = map(int, input().split())
    lines[start].append([end, weight])

start, end = map(int, input().split())
shortest[start] = 0
while not visited[end]:
    min_idx = 0
    min_weight = n * 100000
    for i in range(1, n + 1):
        if visited[i]:
            continue
        if shortest[i] < min_weight:
            min_weight = shortest[i]
            min_idx = i
    visited[min_idx] = True
    shortest[min_idx] = min_weight
    for des, weight in lines[min_idx]:
        shortest[des] = min(shortest[des], min_weight + weight)

print(shortest[end])
