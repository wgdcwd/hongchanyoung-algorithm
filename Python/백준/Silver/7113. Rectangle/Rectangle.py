a, b = map(int, input().split())

ans = 1
while a != b:
    ans += 1
    if a < b:
        a, b = b, a
    a = a - b

print(ans)