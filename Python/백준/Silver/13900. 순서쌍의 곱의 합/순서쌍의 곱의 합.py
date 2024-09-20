n = int(input())
arr = list(map(int, input().split()))
print((sum(arr) ** 2 - sum([i ** 2 for i in arr])) // 2)
