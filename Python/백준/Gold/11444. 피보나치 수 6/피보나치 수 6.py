def fibonacci(n):
    if n < 2:
        return n
    if n in s:
        return s[n]
    ans = 0
    if n % 2 == 0:
        a = fibonacci(n // 2)
        b = fibonacci(n // 2 - 1)
        ans = (a ** 2 + 2 * a * b) % 1000000007
    else:
        a = fibonacci(n // 2)
        b = fibonacci(n // 2 + 1)
        ans = (a ** 2 + b ** 2) % 1000000007

    s[n] = ans
    return ans
s = {}

i = int(input())
print(fibonacci(i) % 1000000007)
