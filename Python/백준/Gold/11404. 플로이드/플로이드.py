import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float("INF") for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], w)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for line in dist:
    for i in line:
        if i == float('INF'):
            print(0, end=" ")
        else:
            print(i, end=" ")
    print()