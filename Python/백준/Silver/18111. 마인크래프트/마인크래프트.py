import sys

n, m, b = map(int, input().split())
cnt = [0 for _ in range(257)]
min_h = 256
max_h = 0
for _ in range(n):
    temp = sys.stdin.readline().strip()
    temp = list(map(int, temp.split()))
    for i in temp:
        if i < min_h:
            min_h = i
        if i > max_h:
            max_h = i
        cnt[i] += 1

ans = [float("inf"), -1]

for height in range(min_h, max_h + 1):
    minus, plus = 0, 0

    for i in range(min_h,max_h + 1):
        sub = i - height
        if sub > 0:
            minus += sub * cnt[i]
        elif sub < 0:
            plus -= sub * cnt[i]

    if plus > b + minus:
        continue
    t = minus * 2 + plus
    if t <= ans[0]:
        ans = [t, height]

print(ans[0], ans[1])
