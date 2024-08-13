n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

ans = 0
for i in arr:
    ans += i // t + (0 if i % t == 0 else 1)

print(ans)
print(n // p, n % p)