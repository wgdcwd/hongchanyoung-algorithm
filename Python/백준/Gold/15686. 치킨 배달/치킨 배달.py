import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
house = []
chicken = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

dist = []
connected_cnt = [0 for _ in range(len(chicken))]
for h in house:
    temp = []
    min_dist = 100
    for c in chicken:
        temp.append(abs(h[0] - c[0]) + abs(h[1] - c[1]))
        if temp[-1] < min_dist:
            min_dist = temp[-1]
    for i in range(len(temp)):
        if temp[i] == min_dist:
            connected_cnt[i] += 1
    dist.append(temp)

#print(house)
#print(chicken)
#print(dist)
#print(connected_cnt)
chicken_n = len(connected_cnt)

if m > len(connected_cnt) - connected_cnt.count(0):
    m = len(connected_cnt) - connected_cnt.count(0)

visited = [(-1 if i == 0 else False) for i in connected_cnt]
ans = [100 * 100]

def cal():
    sum_dist = 0
    for idx, d in enumerate(dist):
        if sum_dist >= ans[0] - len(dist) + idx + 1:
            return
        #print(d)
        #print([d[idx] for idx in range(len(d)) if visited[idx] == True])
        sum_dist += min([d[idx] for idx in range(len(d)) if visited[idx] == True])
    ans[0] = min(ans[0], sum_dist)

def select_chicken(i, start):
    if i == m:

        #ans[0] = min(ans[0], cal())
        #print(visited)

        cal()
        #print(ans)
        return

    for j in range(start, chicken_n):
        if visited[j]:
            continue

        visited[j] = True
        select_chicken(i + 1, j + 1)
        visited[j] = False


select_chicken(0, 0)
print(ans[0])