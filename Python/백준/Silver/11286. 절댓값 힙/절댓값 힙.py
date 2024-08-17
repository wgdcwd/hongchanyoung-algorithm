import sys
import heapq

n = int(input())

q = []

cnt = {}

for _ in range(n):
    i = sys.stdin.readline().strip()
    i = int(i)
    if i == 0:
        if q:
            temp = heapq.heappop(q)
            if cnt[temp] > 0:
                cnt[temp] -= 1
                print(-temp)
            else:
                print(temp)
        else:
            print(0)
    else:
        if i < 0:
            if -i in cnt:
                cnt[-i] += 1
            else:
                cnt[-i] = 1
            heapq.heappush(q, -i)
        else:
            if i in cnt:
                pass
            else:
                cnt[i] = 0
            heapq.heappush(q, i)
