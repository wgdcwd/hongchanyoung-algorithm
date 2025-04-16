n, s = map(int, input().split())

arr = list(map(int, input().split()))

prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[-1] + arr[i])

# print(prefix_sum)

ans = 1000000

start, end = 0, 0
while end != (n + 1):
    # print(prefix_sum[end] - prefix_sum[start])
    if prefix_sum[end] - prefix_sum[start] < s:
        end += 1
    elif prefix_sum[end] - prefix_sum[start] >= s:
        ans = min(ans, end - start)
        start += 1

print(ans if ans != 1000000 else 0)