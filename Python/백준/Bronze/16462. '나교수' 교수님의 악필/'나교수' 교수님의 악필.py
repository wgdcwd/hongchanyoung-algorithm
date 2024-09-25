n = int(input())
arr = [input() for _ in range(n)]
for i in range(n):
    temp = list(arr[i])
    for j in range(len(temp)):
        if temp[j] == '0' or temp[j] == '6':
            temp[j] = '9'

    arr[i] = min(int(''.join(temp)), 100)

ans = (sum(arr) / n)
if ans - ans // 1 >= 0.5:
    print(int(ans) + 1)
else:
    print(int(ans))