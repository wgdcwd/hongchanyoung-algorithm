import math

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)[::-1] + [0]

sub = [arr[i] - arr[i + 1] for i in range(n)]
#print(sub)

sums = [0]
for i in range(n):
    sums.append(sums[-1] + (i + 1) * sub[i])

#print(sums)
start_i = 0 #어느 나무까지만 고려하면 되는지.
for i in range(n):
    if sums[i + 1] >= m:
        start_i = i
        break

need_more = (m - sums[start_i]) / (start_i + 1)
need_more = math.ceil(need_more)
#print(need_more)
print(arr[start_i] - need_more)