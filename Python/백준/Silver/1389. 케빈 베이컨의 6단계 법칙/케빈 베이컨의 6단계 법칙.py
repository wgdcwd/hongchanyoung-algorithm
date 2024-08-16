from collections import deque
import sys

n, m = map(int, input().split())

connects = [[] for _ in range(n)]
for _ in range(m):
    i = sys.stdin.readline().strip()
    a, b = map(int, i.split())
    a, b = a - 1, b - 1
    connects[a].append(b)
    connects[b].append(a)

ans = []
for i in range(n):
    q = deque()
    visited = [False for _ in range(n)]
    for c in connects[i]:
        q.append([c, 1])

    while q:
        person, cnt = q.popleft()
        if visited[person]:
            continue
        visited[person] = cnt

        for c in connects[person]:
            if not visited[c]:
                q.append([c, cnt + 1])

    ans.append(sum(visited))

print(1 + ans.index(min(ans)))