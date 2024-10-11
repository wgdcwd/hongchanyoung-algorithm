n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0]
for i in range(n):
    dp.append(dp[-1] + arr[i])
dp = dp[1:]
dp.sort(reverse=True)
print(sum(dp[:k]))