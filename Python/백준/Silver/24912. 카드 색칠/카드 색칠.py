
n = int(input())

arr = [-1] + list(map(int, input().split())) + [-1]

for i in range(1, n + 1):
    if arr[i] != 0:
        if arr[i] == arr[i - 1]:
            print(-1)
            exit(0)

for i in range(1, n + 1):
    if arr[i] == 0:
        colors = [1, 2, 3]
        if arr[i - 1] in colors:
            colors.remove(arr[i - 1])
        if arr[i + 1] in colors:
            colors.remove(arr[i + 1])
        arr[i] = colors[0]

print(*arr[1:n+1])