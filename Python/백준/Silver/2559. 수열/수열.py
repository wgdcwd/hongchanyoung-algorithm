n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0]
for i in range(n):
    dp.append(dp[-1] + arr[i])
partial_sum = [dp[i + k] - dp[i] for i in range(n - k + 1)]
print(max(partial_sum))