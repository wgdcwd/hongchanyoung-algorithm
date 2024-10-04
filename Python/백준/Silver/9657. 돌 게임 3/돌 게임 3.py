n = int(input())
arr = [False, True, False, True, True, True, True, False, True] + [False] * n


if n < 8:
    pass
else:
    for i in range(8, n + 1):
        arr[i] = False in [arr[i - 1], arr[i - 3], arr[i - 4]]

print("SK" if arr[n] else "CY")