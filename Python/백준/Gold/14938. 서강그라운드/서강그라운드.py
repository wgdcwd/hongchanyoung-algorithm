import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
n_of_items = list(map(int, input().split()))
graph = [[float("INF") for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(r):
    a, b, w = map(int, input().split())
    if graph[a][b] > w:
        graph[a][b] = w
        graph[b][a] = w

#print(graph)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = 0
for line in graph:
    cnt = 0
    for idx, dist in enumerate(line[1:]):
        if dist <= m:
            cnt += n_of_items[idx]

    if ans < cnt:
        ans = cnt

print(ans)