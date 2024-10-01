n = int(input())
if n == 1:
    print(0)
    exit(0)
i = 1
while i * 2 < n:
    i *= 2

if n % 2 == 0:
    print(i - 1 + n // 2)
else:
    print(i - 1 + (n // 2 + 1))