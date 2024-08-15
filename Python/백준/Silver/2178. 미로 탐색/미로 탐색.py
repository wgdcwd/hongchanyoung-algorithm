from collections import deque
import sys
n, m = map(int, input().split())
arr = []
arr.append([0 for _ in range(m + 2)])
for _ in range(n):
    s = sys.stdin.readline().strip()
    s = [int(i) for i in s]
    s = [0] + s + [0]
    arr.append(s)
arr.append([0 for _ in range(m + 2)])


visited = [[False for _ in range(m + 2)] for _ in range(n + 2)]

q = deque()
q.append([1, 1, 1])
while q:
    x, y, c = q.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = True
    if x == n and y == m:
        print(c)
        exit(0)
    directions = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

    for next_x, next_y in directions:
        if not visited[next_x][next_y] and arr[next_x][next_y]:
            q.append([next_x, next_y, c + 1])