import sys

input = sys.stdin.readline

n = int(input())
arr = [input() for _ in range(n)]
ans = []
for i, c in enumerate(arr[0]):
    all_same = True
    for j in range(1, n):
        if c != arr[j][i]:
            all_same = False
            break

    if all_same:
        ans.append(c)
    else:
        ans.append("?")

print("".join(ans))