a, b, c = map(int, input().split())


def func(n):
    if n == 1:
        return a

    if n % 2 == 0:
        return (func(n // 2) ** 2) % c
    else:
        return ((func(n // 2) ** 2) * a) % c

print(func(b) % c)
