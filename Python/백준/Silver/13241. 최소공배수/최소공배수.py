a, b = map(int, input().split())
if b > a:
    a, b = b, a
ans = a * b
while True:
    if a % b == 0:
        ans = ans // b
        break
    a, b = b, a % b

print(ans)