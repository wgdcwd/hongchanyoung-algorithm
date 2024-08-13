import sys
from collections import deque

n = int(input())
arr = deque()
for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 2:
        arr.append(int(temp[1]))
    else:
        if temp[0] == "2":
            if arr:
                print(arr.pop())
            else:
                print(-1)
        elif temp[0] == "3":
            print(len(arr))
        elif temp[0] == "4":
            print((0 if arr else 1))
        elif temp[0] == "5":
            if arr:
                print(arr[-1])
            else:
                print(-1)