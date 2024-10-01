n = int(input())

if n <= 4:
    if n == 1 or n == 3:
        print("CY")
    else:
        print("SK")

    exit(0)

dp = [False for _ in range(n + 1)]
dp[2] = True
dp[4] = True

for i in range(5, n + 1):
    if not dp[i - 1] or not dp[i - 3] or not dp[i - 4]:
        dp[i] = True

print("SK" if dp[n] else "CY")