from collections import deque
import sys

n = int(input())

arr = [[0 for _ in range(n + 2)]]

visited = [[False for _ in range(n + 2)] for _ in range(n + 2)]

for _ in range(n):
    temp = sys.stdin.readline().strip()
    temp = [int(i) for i in temp]
    arr.append([0] + temp + [0])

arr.append([0 for _ in range(n + 2)])


ans = []

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if visited[row][col] or arr[row][col] == 0:
            continue
        q = deque()
        q.append([row, col])

        cnt = 0
        while q:
            r, c = q.popleft()
            if visited[r][c]:
                continue
            visited[r][c] = True
            cnt += 1

            directions = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

            for next_r, next_c in directions:
                if arr[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    q.append([next_r, next_c])

        ans.append(cnt)


ans.sort()
print(len(ans))
for i in ans:
    print(i)