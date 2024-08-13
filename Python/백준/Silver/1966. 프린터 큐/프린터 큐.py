import sys

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = [0] * 10
    for i in arr:
        cnt[i] += 1
    cnt = "".join([str(i) * cnt[i] for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]])
    cnt = [int(c) for c in cnt]
    arr = [[i, arr[i]] for i in range(n)]
    while True:
        if arr[0][1] == cnt[0]:
            cnt.pop(0)
            if arr[0][0] == m:
                print(n - len(cnt))
                break
            arr.pop(0)

        else:
            arr.append(arr.pop(0))

