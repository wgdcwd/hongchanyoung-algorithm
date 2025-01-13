n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = [i[1] for i in sorted(arr)]

dp = [0] * (n + 1)
for i in range(n):
    m = 0
    for j in range(i):
        if arr[j] < arr[i] and dp[j + 1] > m:
            m = dp[j + 1]
    dp[i + 1] = m + 1


print(n - max(dp))