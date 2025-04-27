n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 0
if n % 2 == 0:
    ans = 0
    for i in range(n // 2):
        ans = max(ans, arr[i] + arr[n - 1 - i])
else:
    ans = arr[-1]
    for i in range(n // 2):
        ans = max(ans, arr[i] + arr[n - 2 - i])
print(ans)