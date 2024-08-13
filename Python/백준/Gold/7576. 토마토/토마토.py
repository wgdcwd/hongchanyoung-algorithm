from collections import deque
import sys

m, n = map(int, input().split())
arr = [[-1 for _ in range(m + 2)]]
start = [-1, -1]
q = deque()

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    temp = [-1] + temp + [-1]
    arr.append(temp)

arr.append([-1 for _ in range(m + 2)])


ans = [[False for _ in range(m + 2)] for _ in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == 1:
            q.append([i, j, 0])


while q:
    r, c, d = q.popleft()
    if ans[r][c]:
        continue
    ans[r][c] = d
    direction = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

    for a, b in direction:
        if arr[a][b] == 0 and not ans[a][b]:
            q.append([a, b, d + 1])

max_time = 0

for i in range(1, 1 + n):
    for j in range(1, 1 + m):
        if not ans[i][j]:
            if arr[i][j] == 0:
                print(-1)
                exit(0)
        if ans[i][j] > max_time:
            max_time = ans[i][j]

print(max_time)