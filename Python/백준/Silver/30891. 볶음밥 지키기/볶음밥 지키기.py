import sys
input = sys.stdin.readline
n, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def cal(x, y):
    cnt = 0
    for i, j in arr:
        if (x - i) ** 2 + (y - j) ** 2 <= r ** 2:
            cnt += 1
    return cnt

ans = 0
ans_pos = [-1, -1]
for x in range(-100, 100):
    for y in range(-100, 100):
        temp = cal(x, y)
        if ans < temp:
            ans = temp
            ans_pos = (x, y)

print(*ans_pos)