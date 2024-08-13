n = int(input())

arr = [False for _ in range(n + 1)]
squares = []
i = 1
while i * i <= n:
    squares.append(i * i)
    arr[i * i] = 1
    i += 1


def cal(c):
    if arr[c]:
        return arr[c]

    min_n = 4
    for square in squares[::-1]:
        if square > c:
            continue
        if square < (c / 4):
            break

        min_n = min(cal(c - square) + 1, min_n)
    arr[c] = min_n
    return min_n


print(cal(n))