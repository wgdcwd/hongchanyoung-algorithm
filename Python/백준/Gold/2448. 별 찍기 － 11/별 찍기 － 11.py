n = int(input())


def star(i):
    if i == 3:
        arr = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]
        return arr
    temp = star(i // 2)
    temp_height, temp_width = len(temp), len(temp[0])
    arr = [[" " for _ in range(temp_width * 2 + 1)] for _ in range(i)]

    start_pos = [[0, temp_width // 2 + 1], [temp_height, 0], [temp_height, temp_width + 1]]
    for start_r, start_c in start_pos:
        for i in range(temp_height):
            for j in range(temp_width):
                arr[i + start_r][j + start_c] = temp[i][j]

    return arr


ans = star(n)
for line in ans:
    print("".join(line))
