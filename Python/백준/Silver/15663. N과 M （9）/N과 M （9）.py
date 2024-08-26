import sys
from collections import deque

n, m = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
ans = set()

def recur(s: deque, c):
    if c == m:
        ans.add(" ".join(str(c) for c in list(s)))
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        s.append(arr[i])
        recur(s, c + 1)
        s.pop()
        visited[i] = False


recur(deque(), 0)
ans = sorted([list(map(int, s.split())) for s in ans])
for i in ans:
    print(*i)