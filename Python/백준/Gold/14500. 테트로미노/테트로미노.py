import sys
from collections import deque

n, m = map(int, input().split())

arr = [[0 for _ in range(m + 2)]]

for _ in range(n):
    i = sys.stdin.readline().strip().split()
    i = [0] + list(map(int, i)) + [0]
    arr.append(i)

arr.append([0 for _ in range(m + 2)])

ans = []

for i in range(1, n + 1):
    for j in range(1, m):
        sum_all = arr[i][j] + arr[i][j + 1]
        another = [arr[i][j - 1], arr[i][j + 2], arr[i + 1][j], arr[i + 1][j + 1], arr[i - 1][j], arr[i - 1][j + 1]]
        another = sorted(another)
        sum_all += another[-1] + another[-2]
        ans.append(sum_all)

for i in range(1, n):
    for j in range(1, m + 1):
        sum_all = arr[i][j] + arr[i + 1][j]
        another = [arr[i - 1][j], arr[i + 2][j], arr[i][j - 1], arr[i][j + 1], arr[i + 1][j - 1], arr[i + 1][j + 1]]
        another = sorted(another)
        sum_all += another[-1] + another[-2]
        ans.append(sum_all)

print(max(ans))
