a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a1, b1, a2, b2 = b2 * a1, b2 * b1, b1 * a2, b1 * b2
a, b = a1 + a2, b1

def cal(x, y):
    if y > x:
        x, y = y, x

    while True:
        if x % y == 0:
            return y

        x, y = y, x % y

div = cal(a, b)
print(a // div, b // div)

