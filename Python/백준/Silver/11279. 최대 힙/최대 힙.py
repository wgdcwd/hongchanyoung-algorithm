import heapq
import sys

n = int(input())
arr = []

for _ in range(n):
    temp = sys.stdin.readline().strip()
    temp = int(temp)
    if temp == 0:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, -temp)

