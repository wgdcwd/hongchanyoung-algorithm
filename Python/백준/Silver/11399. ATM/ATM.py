n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
ans = 0
curr_sum = 0
for i in arr:
    ans += curr_sum + i
    curr_sum += i
print(ans)