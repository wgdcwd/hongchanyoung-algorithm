import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
reversed_arr = []
for i in arr[::-1]:
    if i == 1:
        reversed_arr.append(3)
    elif i == 2:
        reversed_arr.append(4)
    elif i == 3:
        reversed_arr.append(1)
    elif i == 4:
        reversed_arr.append(2)


def is_same(a, b):
    for i in range(len(b)):
        for j in range(len(a)):
            if a[j] != b[(i + j) % len(b)]:
                break
            if j == len(a) - 1:
                return True
    return False

ans = []
for _ in range(int(input())):
    s = list(map(int, input().split()))
    if is_same(arr, s) or is_same(reversed_arr, s):
        ans.append(s)

print(len(ans))
for i in ans:
    print(*i)