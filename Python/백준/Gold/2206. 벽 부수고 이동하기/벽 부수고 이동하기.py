import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[-1 for _ in range(m + 2)]]
for _ in range(n):
    board.append([-1] + [int(i) for i in input().strip()] + [-1])
board.append([-1 for _ in range(m + 2)])

visited = [[[False for _ in range(m + 2)] for _ in range(n + 2)] for _ in range(2)]

q = deque()
q.append([1, 1, 0, 0])

while q:
    r, c, remove_wall, cnt = q.popleft()
    if visited[remove_wall][r][c]:
        continue
    if r == n and c == m:
        print(cnt + 1)
        exit(0)

    visited[remove_wall][r][c] = True
    direction = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

    if remove_wall == 0:
        for next_r, next_c in direction:
            if board[next_r][next_c] == 0 and not visited[0][next_r][next_c]:
                q.append([next_r, next_c, 0, cnt + 1])
            elif board[next_r][next_c] == 1 and not visited[1][next_r][next_c]:
                q.append([next_r, next_c, 1, cnt + 1])
    else:
        for next_r, next_c in direction:
            if board[next_r][next_c] == 0 and not visited[1][next_r][next_c]:
                q.append([next_r, next_c, 1, cnt + 1])

print(-1)