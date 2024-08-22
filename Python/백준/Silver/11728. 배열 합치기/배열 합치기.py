n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = a + b
arr = sorted(arr)
print(*arr)