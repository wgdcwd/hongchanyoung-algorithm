n = int(input())
ans = 1
for i in range(1, n, 2):
    ans *= i
print(ans % 1000000007)