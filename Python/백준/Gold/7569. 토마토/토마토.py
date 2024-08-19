import sys
from collections import deque

m, n, h = map(int, input().split())

arr = [[[-1 for _ in range(m + 2)] for _ in range(n + 2)]]
q = deque()

for i in range(h):
    temp = [[-1 for _ in range(m + 2)]]
    for j in range(n):
        temp.append([-1] + list(map(int, sys.stdin.readline().strip().split())) + [-1])
    temp.append([-1 for _ in range(m + 2)])
    arr.append(temp)
arr.append([[-1 for _ in range(m + 2)] for _ in range(n + 2)])


#ans = [[[-1 for _ in range(m + 2)] for _ in range(n + 2)] for _ in range(h + 2)]
#visited = [[[False for _ in range(m + 2)] for _ in range(n + 2)] for _ in range(h + 2)]
zero_n = 0
cnt = 0
for i in range(1, h + 1):
    for j in range(1, n + 1):
        for k in range(1, m + 1):
            if arr[i][j][k] == 1:
                #ans[i][j][k] = 1
                q.append([i, j, k, 1])
                arr[i][j][k] = 0
                cnt -= 1
            elif arr[i][j][k] == 0:
                #ans[i][j][k] = 0
                zero_n += 1


# for layer in arr:
#     for line in layer:
#         print(*line)
#
#     print("----------------")
ans = 1
#(q)
while q:
    #print("q")
    i, j, k, time = q.popleft()
    #if visited[i][j][k]:
    if arr[i][j][k] != 0:
        continue
    #visited[i][j][k] = True
    cnt += 1
    arr[i][j][k] = time
    ans = max(ans, time)

    directions = [[i - 1, j, k], [i + 1, j, k], [i, j - 1, k], [i, j + 1, k], [i, j, k - 1], [i, j, k + 1]]
    for v in directions:
        if arr[v[0]][v[1]][v[2]] == 0:
            q.append([v[0], v[1], v[2], time + 1])

print((-1 if cnt != zero_n else (ans - 1)))
#print(zero_n, cnt)