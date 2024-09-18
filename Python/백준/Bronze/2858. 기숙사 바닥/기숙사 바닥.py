r, b = map(int, input().split())
xy = r + b
xpy = (r + 4) // 2

y = 1
x = xpy - 1
while x * y != xy or x == 0:
    y += 1
    x -= 1

print(x, y)