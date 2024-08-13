import sys
from collections import deque
n, m, v = map(int, input().split())

lines = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    lines[a].append(b)
    lines[b].append(a)


for line in lines:
    line.sort()

stk = [v]
while stk:
    k = stk.pop()
    if visited[k]:
        continue
    visited[k] = True
    print(k, end=" ")
    arr = lines[k][::-1]
    for start in arr:
        if visited[start]:
            continue
        stk.append(start)

print()

visited = [False for _ in range(n + 1)]
que = deque()
que.append(v)

while que:
    k = que.popleft()
    if visited[k]:
        continue
    visited[k] = True
    print(k, end=" ")
    arr = lines[k]
    for start in arr:
        if visited[start]:
            continue
        que.append(start)