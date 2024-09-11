n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())

for line in arr:
    print(line[::-1])