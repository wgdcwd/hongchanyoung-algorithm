n = int(input())
arr = list(map(int, input().split()))

f, b = 0, n - 1
ans = [2000000000, f, b]
while f != b:
    if ans[0] > abs(arr[f] + arr[b]):
        ans = [abs(arr[f] + arr[b]), f, b]
    if abs(arr[f]) > abs(arr[b]):
        f += 1
    elif abs(arr[b]) > abs(arr[f]):
        b -= 1
    else:
        ans = [abs(arr[f] + arr[b]), f, b]
        break

# print(ans)
print(arr[ans[1]], arr[ans[2]])