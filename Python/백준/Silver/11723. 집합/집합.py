import sys
n = int(input())
arr = [False] * 21

for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == "all":
        arr = [True] * 21
    elif s == "empty":
        arr = [False] * 21
    else:
        cal, i = s.split()
        i = int(i)
        if cal == "add":
            arr[i] = True
        elif cal == "remove":
            arr[i] = False
        elif cal == "check":
            print(1 if arr[i] else 0)
        elif cal == "toggle":
            arr[i] = not arr[i]