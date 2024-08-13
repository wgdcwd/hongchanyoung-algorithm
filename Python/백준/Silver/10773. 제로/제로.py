n = int(input())
arr = []
for _ in range(n):
    i = int(input())
    if i == 0:
        arr.pop()
    else:
        arr.append(i)
print(sum(arr))