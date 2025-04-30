t = int(input())
n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
if t <= s:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")