from collections import deque
import sys
import time

n, m = map(int, input().split())
arr = [[0 for _ in range(m + 2)]]
start = [-1, -1]
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    temp = [0] + temp + [0]
    if 2 in arr[-1]:
        start = [len(arr) - 1, arr[-1].index(2)]
    arr.append(temp)
arr.append([0 for _ in range(m + 2)])

ans = [[False for _ in range(m + 2)] for _ in range(n + 2)]

start = start + [0]
q = deque()
q.append(start)


while q:
    r, c, d = q.popleft()
    if ans[r][c]:
        continue
    ans[r][c] = d

    direction = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

    for a, b in direction:
        if arr[a][b] == 1 and not ans[a][b]:
            q.append([a, b, d + 1])

for i in range(1, 1 + n):
    for j in range(1, 1 + m):
        if not ans[i][j]:
            if arr[i][j] == 0 or arr[i][j] == 2:
                print(0, end=" ")
            else:
                print(-1, end=" ")
        else:
            print(ans[i][j], end=" ")
    print()
