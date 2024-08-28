from collections import deque

n, m = map(int, input().split())

if n >= m:
    print(n - m)
    exit(0)

visited = [False for _ in range(m + n + 1)]

q = deque()
q.append([n, 0])

while q:
    curr, cnt = q.popleft()
    if curr == m:
        print(cnt)
        break

    if visited[curr]:
        continue
    visited[curr] = True

    if curr * 2 < n + m + 1:
        q.appendleft([curr * 2, cnt])
    if curr + 1 < n + m + 1:
        q.append([curr + 1, cnt + 1])
    if curr - 1 >= 0:
        q.append([curr - 1, cnt + 1])