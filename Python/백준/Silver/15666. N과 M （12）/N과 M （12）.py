import sys
from collections import deque

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
n = len(arr)

ans = set()


def recur(s: deque, c, end):
    if c == m:
        ans.add(" ".join(str(c) for c in list(s)))
        return

    for i in range(end, n):
        s.append(arr[i])
        recur(s, c + 1, i)
        s.pop()


recur(deque(), 0, 0)
ans = sorted([list(map(int, s.split())) for s in ans])
for i in ans:
    print(*i)
