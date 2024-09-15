from collections import deque
import sys

input = sys.stdin.readline
n, m, t = map(int, input().split())

area = [[-1 for _ in range(m + 2)]]
for _ in range(n):
    area.append([-1] + list(map(int, input().split())) + [-1])
area.append([-1 for _ in range(m + 2)])

cleaner_pos = [-1, -1]
for r in range(1, n + 1):
    if area[r][1] == -1:
        cleaner_pos = [r, r + 1]
        break

#print(cleaner_pos)


def circulation():
    #upper circle
    for i in range(cleaner_pos[0] - 1, 1, -1):
        area[i][1] = area[i - 1][1]

    for i in range(1, m):
        area[1][i] = area[1][i + 1]

    for i in range(1, cleaner_pos[0]):
        area[i][m] = area[i + 1][m]

    for i in range(m, 1, -1):
        area[cleaner_pos[0]][i] = area[cleaner_pos[0]][i - 1]
    area[cleaner_pos[0]][2] = 0

    #lower circle
    for i in range(cleaner_pos[1] + 1, n):
        area[i][1] = area[i + 1][1]

    for i in range(1, m):
        area[n][i] = area[n][i + 1]

    for i in range(n, cleaner_pos[1], -1):
        area[i][m] = area[i - 1][m]

    for i in range(m, 1, -1):
        area[cleaner_pos[1]][i] = area[cleaner_pos[1]][i - 1]
    area[cleaner_pos[1]][2] = 0


def diffusion():
    change_table = [[-1 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            change_table[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if area[i][j] == -1:
                continue
            cnt = area[i][j]
            direction = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            for near_r, near_c in direction:
                if area[near_r][near_c] != -1:
                    change_table[near_r][near_c] += area[i][j] // 5
                    cnt -= area[i][j] // 5
            change_table[i][j] += cnt
    change_table[cleaner_pos[0]][1] = -1
    change_table[cleaner_pos[1]][1] = -1

    return change_table


for _ in range(t):
    area = diffusion()
    circulation()

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ans += area[i][j]

# for line in area[1:n+1]:
#     print(line[1:m+1])

print(ans + 2)
