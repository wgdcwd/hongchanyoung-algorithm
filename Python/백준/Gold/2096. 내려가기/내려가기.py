import sys

input = sys.stdin.readline

n = int(input())
min_dp = [0, 0, 0]
min_temp = [0, 0, 0]
max_dp = [0, 0, 0]
max_temp = [0, 0, 0]

for _ in range(n):
    board = list(map(int, input().split()))

    max_temp[0] = max(max_dp[0], max_dp[1]) + board[0]
    max_temp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + board[1]
    max_temp[2] = max(max_dp[2], max_dp[1]) + board[2]
    max_dp[0] = max_temp[0]
    max_dp[1] = max_temp[1]
    max_dp[2] = max_temp[2]

    min_temp[0] = min(min_dp[0], min_dp[1]) + board[0]
    min_temp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + board[1]
    min_temp[2] = min(min_dp[2], min_dp[1]) + board[2]
    min_dp[0] = min_temp[0]
    min_dp[1] = min_temp[1]
    min_dp[2] = min_temp[2]

print(max(max_dp), end=" ")
print(min(min_dp))
