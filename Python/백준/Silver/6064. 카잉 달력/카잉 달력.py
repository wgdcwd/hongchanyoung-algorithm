import sys

t = int(input())


def gcd(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b
    return b


for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().strip().split())
    if m > n:
        m, n, x, y = n, m, y, x

    last = m * n // gcd(m, n)

    k = y
    find = False
    #n >
    while k <= last:
        if (k - y) % n == 0 and (k - x) % m == 0:
            print(k)
            find = True
            break
        k += n

    if not find:
        print(-1)

# n, m, x, y = 5, 100, 4, 18
# for i in range(n * m):
#     print((y + m * i) % n)
