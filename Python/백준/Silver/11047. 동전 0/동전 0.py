n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

ans = 0
for i in arr[::-1]:
    ans += k // i
    k = k % i

print(ans)