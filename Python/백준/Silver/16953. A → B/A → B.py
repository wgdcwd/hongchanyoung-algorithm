from collections import deque
a, b = map(int, input().split())

q = deque()
q.append([a, 0])

ans = -1
while q:
    n, c = q.popleft()
    if n > b:
        continue
    if n == b:
        ans = c + 1
        break
    q.append([n * 2, c + 1])
    q.append([n * 10 + 1, c + 1])

print(ans)