n, k = map(int, input().split())
arr = {}
for _ in range(n):
    addr, password = input().split()
    arr[addr] = password

for _ in range(k):
    print(arr[input()])