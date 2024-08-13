a, b, c, d, e, f = map(int, input().split())

find = False
x = 999
y = 999
while True:
    while y > -1000:
        if a * x + b * y == c and d * x + e * y == f:
            find = True
            break
        y -= 1
    if find:
        break
    x -= 1
    y = 999

print(x, y)