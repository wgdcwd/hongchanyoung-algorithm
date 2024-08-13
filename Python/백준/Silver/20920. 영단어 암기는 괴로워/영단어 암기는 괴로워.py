from functools import cmp_to_key
import sys

n, m = map(int, input().split())
d = {}

def compare(x, y):
    if x[1] > y[1]:
        return 1
    elif x[1] < y[1]:
        return -1
    if len(x[0]) > len(y[0]):
        return 1
    elif len(x[0]) < len(y[0]):
        return -1
    if x[0] < y[0]:
        return 1
    else:
        return -1


for _ in range(n):
    i = sys.stdin.readline().strip()
    if len(i) < m:
        continue
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


arr = d.items()
arr = sorted(arr, key = cmp_to_key(compare))
for i in arr[::-1]:
    print(i[0])