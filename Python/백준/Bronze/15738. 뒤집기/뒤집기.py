n, k, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    i = int(input())
    if i > 0:
        if k <= i:
            k = i - k + 1
    else:
        if n + i < k:
            k = (n + i) + (n - k + 1)

print(k)
