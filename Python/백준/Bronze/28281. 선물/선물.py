n, x = map(int, input().split())
arr = list(map(int, input().split()))
s = [arr[i] + arr[i + 1] for i in range(n - 1)]
print(min(s) * x)