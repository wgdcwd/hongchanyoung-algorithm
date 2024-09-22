from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[-1 for _ in range(m + 2)]]
for _ in range(n):
    temp = [-1] + list(map(int, input().split())) + [-1]
    arr.append(temp)
arr.append([-1] * (m + 2))

# cheese = []
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if arr[i][j] == 1:
#             cheese.append((i, j))

def outer_air(air_poses):
    q = deque()
    for air_row, air_col in air_poses:
        q.append((air_row, air_col))
    while q:
        curr_row, curr_col = q.popleft()
        if  arr[curr_row][curr_col] == -1:
            continue

        arr[curr_row][curr_col] = -1

        direction = [[curr_row - 1, curr_col], [curr_row + 1, curr_col], [curr_row, curr_col - 1], [curr_row, curr_col + 1]]
        for next_row, next_col in direction:
            if arr[next_row][next_col] == 0:
                q.append((next_row, next_col))


# for line in arr[1:n + 1]:
#     print(*line[1:m + 1])
# outer_air([[1, 1]])
# print()
# for line in arr[1:n + 1]:
#     print(*line[1:m + 1])

ans = 0
outer_air([[1, 1]])
while True:
    temp = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] != 1:
                continue

            cnt = 0
            direction = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
            for r, c in direction:
                if arr[r][c] == -1:
                    cnt += 1

            if cnt >= 2:
                arr[i][j] = 0
                temp.append((i, j))

    if not temp:
        break
    outer_air(temp)
    ans += 1

print(ans)