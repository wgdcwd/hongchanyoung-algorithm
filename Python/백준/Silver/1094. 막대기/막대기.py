n = int(input())
ans = 0
stick = 64
while n > 0:
    if n < stick:
        stick = stick // 2
        continue

    ans += n // stick
    n = n % stick

print(ans)