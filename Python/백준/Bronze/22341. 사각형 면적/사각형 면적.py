n, c = map(int, input().split())
row, col = n, n
for _ in range(c):
    x, y = map(int, input().split())
    if x > row or y > col:
        continue
    cut_horizontal = True if (col * x) >= (row * y) else False
    if cut_horizontal:
        row = x
    else:
        col = y

print(row * col)