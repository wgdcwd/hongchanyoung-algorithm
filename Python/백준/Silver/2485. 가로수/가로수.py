n = int(input())

points = []
dist = []
for i in range(n):
    points.append(int(input()))

for i in range(n - 1):
    dist.append(points[i + 1] - points[i])


def cal(x, y):
    if x < y:
        x, y = y, x

    while True:
        if x % y == 0:
            return y

        x, y = y, x % y


gcd = cal(dist[0], dist[1])
for i in dist[2:]:
    gcd = cal(i, gcd)

ans = 0
for i in dist:
    ans += i // gcd - 1
print(ans)