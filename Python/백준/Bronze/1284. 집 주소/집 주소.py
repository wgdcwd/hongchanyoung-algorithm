arr = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]
while True:
    i = input()
    if i == "0":
        break
    ans = 0
    for c in i:
        ans += arr[int(c)]
    ans += len(i) + 1
    print(ans)