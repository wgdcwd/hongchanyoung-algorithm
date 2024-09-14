from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

area = [[1 for _ in range(m + 2)]]
for _ in range(n):
    area.append([1] + list(map(int, input().split())) + [1])
area.append([1 for _ in range(m + 2)])

warning_place = []
wall_count = 3
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if area[i][j] == 1:
            wall_count += 1
        elif area[i][j] == 2:
            warning_place.append([i, j])


def bfs(copied):
    q = deque()
    warning_count = 0
    for row, col in warning_place:
        copied[row][col] = 0
        q.append([row, col])

    while q:
        r, c = q.popleft()
        if copied[r][c] != 0:
            continue
        copied[r][c] = 2
        warning_count += 1
        next_pos = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
        for next_r, next_c in next_pos:
            if copied[next_r][next_c] == 0:
                q.append([next_r, next_c])

    return n * m - warning_count - wall_count


max_range = (n + 2) * (m + 2)
ans = 0

for fst_wall in range(max_range):
    fst_row, fst_col = fst_wall // (m + 2), fst_wall % (m + 2)
    if area[fst_row][fst_col] != 0:
        continue
    for snd_wall in range(fst_wall + 1, max_range):
        snd_row, snd_col = snd_wall // (m + 2), snd_wall % (m + 2)
        if area[snd_row][snd_col] != 0:
            continue
        for tnd_wall in range(snd_wall + 1, max_range):
            tnd_row, tnd_col = tnd_wall // (m + 2), tnd_wall % (m + 2)
            if area[tnd_row][tnd_col] != 0:
                continue

            area[fst_row][fst_col] = 1
            area[snd_row][snd_col] = 1
            area[tnd_row][tnd_col] = 1
            ans = max(ans, bfs([line[:] for line in area]))
            area[fst_row][fst_col] = 0
            area[snd_row][snd_col] = 0
            area[tnd_row][tnd_col] = 0

print(ans)