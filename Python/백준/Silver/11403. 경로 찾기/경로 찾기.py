import sys
from collections import deque
n = int(input())

lines = [[]for _ in range(n)]

for i in range(n):
    s = sys.stdin.readline().strip().split()
    for j in range(n):
        if s[j] == "1":
            lines[i].append(j)

ans = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    q = deque()

    visited = [False for _ in range(n)]

    if lines[i]:
        for j in lines[i]:
            q.append(j)

    while q:
        u = q.popleft()
        if visited[u]:
            continue
        visited[u] = True
        ans[i][u] = 1

        if lines[u]:
            for j in lines[u]:
                if not visited[j]:
                    q.append(j)

for i in ans:
    for j in i:
        print(j, end=" ")
    print()