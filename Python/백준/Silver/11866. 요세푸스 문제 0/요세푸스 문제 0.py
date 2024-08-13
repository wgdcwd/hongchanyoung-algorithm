n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
curr = 0
ans = []
while arr:
    curr = (curr + m - 1) % len(arr)
    ans.append(arr[curr])
    arr = arr[:curr] + arr[curr + 1:]

s = ", ".join(str(i) for i in ans)
s = "<" + s + ">"
print(s)