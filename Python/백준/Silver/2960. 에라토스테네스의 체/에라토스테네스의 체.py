n, k = map(int, input().split())

arr = [True for _ in range(n + 1)]
arr[0] = False
arr[1] = False
ans = []
i = 1
while i < n:
    i += 1
    if not arr[i]:
        continue
    ans.append(i)
    arr[i] = False
    j = 2 * i
    while j < n + 1:
        if arr[j]:
            arr[j] = False
            ans.append(j)
        j += i

print(ans[k - 1])