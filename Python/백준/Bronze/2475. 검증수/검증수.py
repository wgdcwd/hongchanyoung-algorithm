arr = list(map(int, input().split()))
arr = [i * i for i in arr]
print(sum(arr) % 10)