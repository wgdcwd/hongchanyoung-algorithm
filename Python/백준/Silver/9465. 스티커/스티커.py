import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())), list(map(int, input().split()))]

    dp = [[0 for _ in range(n + 2)] for _ in range(2)]
    for i in range(n):
        dp[0][i + 2] = max(dp[1][i], dp[1][i + 1]) + arr[0][i]
        dp[1][i + 2] = max(dp[0][i], dp[0][i + 1]) + arr[1][i]

    print(max(dp[0][n], dp[1][n], dp[0][n + 1], dp[1][n + 1]))