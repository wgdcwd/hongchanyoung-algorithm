import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

visited = [False] * (n + 1)
arr = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)

ans = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    ans += 1
    visited[i] = True
    q = deque(arr[i])
    arr[i] = []
    while q:
        node = q.pop()
        if visited[node]:
            continue
        q.extend(arr[node])
        arr[node] = []
        visited[node] = True

print(ans)
