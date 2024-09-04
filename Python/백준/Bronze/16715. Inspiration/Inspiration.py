n = int(input())
ans = [-1, -1]
for i in range(2, n + 1):
    temp = n
    cnt = 0
    while temp:
        cnt += temp % i
        temp = temp // i
    if ans[0] < cnt:
        ans = [cnt, i]

print(*ans)