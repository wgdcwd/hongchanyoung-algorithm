r, c, n = map(int, input().split())
r = r // n + (0 if r % n == 0 else 1)
c = c // n + (0 if c % n == 0 else 1)
print(r * c)