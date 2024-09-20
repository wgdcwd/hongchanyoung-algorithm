import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, m, s = map(int, input().split())
    s = 360 * s / 60
    m = 360 * m / 60 + 6 * (s / 360)
    h = 360 * h / 12 + 30 * (m / 360)

    a = abs(h - m)
    b = abs(m - s)
    c = abs(s - h)
    a = min(a, 360 - a)
    b = min(b, 360 - b)
    c = min(c, 360 - c)
    ans = min(a, b, c)
    print(ans)
