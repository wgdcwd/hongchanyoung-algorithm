n, m = map(int, input().split())
row = []
for _ in range(n - 1):
    row.append(int(input()))

col = list(map(int, input().split()))
row.append(col[0])

print(1 + row.index(min(row)), 1 + col.index(min(col)))