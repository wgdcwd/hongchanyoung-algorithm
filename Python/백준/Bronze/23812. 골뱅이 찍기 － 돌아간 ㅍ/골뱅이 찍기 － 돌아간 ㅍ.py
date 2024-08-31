n = int(input())

arr = [["@" for _ in range(n * 5)] for _ in range(n * 5)]

for i in range(0, n):
    for j in range(n, n * 4):
        arr[i][j] = " "

for i in range(2 * n, 3 * n):
    for j in range(n, n * 4):
        arr[i][j] = " "

for i in range(4 * n, 5 * n):
    for j in range(n, n * 4):
        arr[i][j] = " "

for i in range(5 * n):
    for j in range(5 * n):
        print(arr[i][j], end="")
    print()