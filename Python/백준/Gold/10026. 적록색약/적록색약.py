import sys
from collections import deque

n = int(input())

arr = [["N" for _ in range(n + 2)]]

for _ in range(n):
    temp = sys.stdin.readline().strip()
    temp = ["N"] + list(temp) + ["N"]
    arr.append(temp)
arr.append(["N" for _ in range(n + 2)])

visited = [[False for _ in range(n + 2)] for _ in range(n + 2)]

rgb, rg_or_b = 0, 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not visited[i][j]:
            rgb += 1
            now = arr[i][j]
            q = deque()
            q.append([i, j, now])

            while q:
                r, c, color = q.popleft()
                if visited[r][c]:
                    continue
                else:
                    visited[r][c] = True

                    directions = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

                    for next_r, next_c in directions:
                        if visited[next_r][next_c]:
                            continue
                        if arr[next_r][next_c] != color:
                            continue
                        q.append([next_r, next_c, color])

visited = [[False for _ in range(n + 2)] for _ in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not visited[i][j]:
            rg_or_b += 1
            now = arr[i][j]
            q = deque()
            q.append([i, j, now])

            while q:
                r, c, color = q.popleft()
                if visited[r][c]:
                    continue
                else:
                    visited[r][c] = True

                    directions = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

                    for next_r, next_c in directions:
                        if visited[next_r][next_c]:
                            continue
                        if arr[next_r][next_c] == "N":
                            continue
                        if arr[next_r][next_c] == "B" and arr[next_r][next_c] == color:
                            q.append([next_r, next_c, color])
                        elif arr[next_r][next_c] in ["R", "G"] and color in ["R", "G"]:
                            q.append([next_r, next_c, color])

print(rgb, rg_or_b)