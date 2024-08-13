from collections import deque
import sys

n = int(input())

q = deque([])

for _ in range(n):
    i = sys.stdin.readline().strip()
    if i == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif i == "size":
        print(len(q))
    elif i == "empty":
        print(0 if q else 1)
    elif i == "front":
        print(q[0] if q else -1)
    elif i == "back":
        print(q[-1] if q else -1)
    else:
        _, i = i.split()
        q.append(i)