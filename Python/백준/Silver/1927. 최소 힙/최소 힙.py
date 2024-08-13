import sys
import heapq

n = sys.stdin.readline().strip()
n = int(n)
arr = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)
