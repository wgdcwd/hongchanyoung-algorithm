n = int(input())

ans = 0
cnt = 1
for i in range(n - 3):
    ans += (cnt * cnt + cnt) // 2
    cnt += 1
print(ans * n // 4)