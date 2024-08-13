from collections import deque
import sys

n, m = map(int, input().split())
visited = [[False for _ in range(m + 2)] for _ in range(n + 2)]
arr = [["X" for _ in range(m + 2)]]
start = []
for i in range(n):
    arr.append(["X"] + [c for c in sys.stdin.readline().strip()] + ["X"])
    if "I" in arr[-1]:
        start = [i + 1, arr[-1].index("I")]
arr.append(["X" for _ in range(m + 2)])

q = deque()
q.append(start)
ans = 0
while q:
    r, c = q.popleft()
    if visited[r][c]:
        continue
    visited[r][c] = True
    if arr[r][c] == "P":
        ans += 1
    direction = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
    for move_r, move_c in direction:
        if not visited[move_r][move_c] and arr[move_r][move_c] != "X":
            q.append([move_r, move_c])

if ans == 0:
    print("TT")
else:
    print(ans)