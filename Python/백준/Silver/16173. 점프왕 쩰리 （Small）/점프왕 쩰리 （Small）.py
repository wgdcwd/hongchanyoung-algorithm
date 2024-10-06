n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

q = deque()
q.append([0, 0])

ans = False
while q:
    r, c = q.pop()
    if r == n - 1 and c == n - 1:
        ans = True
        break
    if board[r][c] == 0:
        continue

    if r + board[r][c] < n:
        q.append([r + board[r][c], c])

    if c + board[r][c] < n:
        q.append([r, c + board[r][c]])

print("HaruHaru" if ans else "Hing")