from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = [[10 for _ in range(n + 2)]]
for _ in range(n):
    arr.append([10] + list(map(int, input().split())) + [10])
arr.append([10 for _ in range(n + 2)])

shark_r = [-1]
shark_c = [-1]
shark_size = [2]
eat_stack = [0]
time = [0]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 9:
            shark_r[0] = i
            shark_c[0] = j
            arr[i][j] = 0
            break


def search():
    visited = [[False for _ in range(n + 2)] for _ in range(n + 2)]
    q = deque()
    q.append([shark_r[0], shark_c[0], 0])
    temp = []

    while q:
        curr_r, curr_c, t = q.popleft()
        if visited[curr_r][curr_c]:
            continue
        visited[curr_r][curr_c] = True
        if 0 < arr[curr_r][curr_c] < shark_size[0]:
            temp.append([curr_r, curr_c, t])

        directions = [[curr_r - 1, curr_c], [curr_r + 1, curr_c], [curr_r, curr_c - 1], [curr_r, curr_c + 1]]

        for next_r, next_c in directions:
            if visited[next_r][next_c]:
                continue
            if arr[next_r][next_c] <= shark_size[0]:
                q.append([next_r, next_c, t + 1])

    if not temp:
        return False
    for i in range(len(temp) - 1, 0, -1):
        if temp[i][2] != temp[0][2]:
            temp.pop()
            continue
        break
    temp.sort()
    arr[temp[0][0]][temp[0][1]] = 0
    time[0] += temp[0][2]
    eat_stack[0] += 1
    shark_r[0] = temp[0][0]
    shark_c[0] = temp[0][1]
    if eat_stack[0] == shark_size[0]:
        eat_stack[0] = 0
        shark_size[0] = min(shark_size[0] + 1, 7)

    return True


while search():
    pass

print(*time)