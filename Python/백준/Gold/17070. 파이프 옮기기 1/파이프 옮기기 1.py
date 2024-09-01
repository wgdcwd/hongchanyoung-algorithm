import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = [[1 for _ in range(n + 2)]]

for _ in range(n):
    temp = [1] + list(map(int, input().split())) + [1]
    arr.append(temp)

arr.append([1 for _ in range(n + 2)])

dp = [[[False, False, False] for _ in range(n + 2)] for _ in range(n + 2)]
for i in range(n + 2):
    dp[i][1] = [0, 0, 0]
dp[1][2] = [1, 0, 0]


def cal(row, col, state):
    if dp[row][col][state]:
        return dp[row][col][state]
    if arr[row][col] == 1:
        return 0
    temp = 0
    if state == 0:
        if arr[row][col - 1] == 0:
            temp += cal(row, col - 1, 0)
            temp += cal(row, col - 1, 2)
    elif state == 1:
        if arr[row - 1][col] == 0:
            temp += cal(row - 1, col, 1)
            temp += cal(row - 1, col, 2)
    elif state == 2:
        if arr[row - 1][col] == 0 and arr[row][col - 1] == 0 and arr[row - 1][col - 1] == 0:
            temp += cal(row - 1, col - 1, 0)
            temp += cal(row - 1, col - 1, 1)
            temp += cal(row - 1, col - 1, 2)

    dp[row][col][state] = temp
    return dp[row][col][state]


a = cal(n, n, 0)
b = cal(n, n, 1)
c = cal(n, n, 2)
print(a + b + c)
