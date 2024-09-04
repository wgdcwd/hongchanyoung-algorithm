import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if x3 <= x1:
        x3 = x1
    elif x3 >= x2:
        x3 = x2
    if x4 <= x1:
        x4 = x1
    elif x4 >= x2:
        x4 = x2
    if y3 <= y1:
        y3 = y1
    elif y3 >= y2:
        y3 = y2
    if y4 <= y1:
        y4 = y1
    elif y4 >= y2:
        y4 = y2
    print((x2 - x1) * (y2 - y1) - (x4 - x3) * (y4 - y3))