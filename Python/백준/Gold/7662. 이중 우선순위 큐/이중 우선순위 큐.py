import sys
import heapq

input = sys.stdin.readline
for _ in range(int(input())):
    s, l = [], []
    i, d = 0, 0
    nums = {}
    for _ in range(int(input())):
        f, n = input().strip().split()
        n = int(n)

        if f == "I":
            i += 1
            heapq.heappush(s, n)
            heapq.heappush(l, -n)
            if n in nums:
                nums[n] += 1
            else:
                nums[n] = 1
        if f == "D":
            if n == -1:
                while True:
                    if not s:
                        break
                    temp = heapq.heappop(s)
                    if nums[temp] > 0:
                        nums[temp] -= 1
                        d += 1
                        break
            elif n == 1:
                while True:
                    if not l:
                        break
                    temp = -heapq.heappop(l)
                    if nums[temp] > 0:
                        nums[temp] -= 1
                        d += 1
                        break


    if i <= d:
        print("EMPTY")
    else:
        a = 0
        while True:
            temp = -heapq.heappop(l)
            if nums[temp] > 0:
                a = temp
                break

        b = 0
        while True:
            temp = heapq.heappop(s)
            if nums[temp] > 0:
                b = temp
                break
        print(a, b)
