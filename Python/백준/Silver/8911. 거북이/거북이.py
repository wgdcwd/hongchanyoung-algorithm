v = [[1, 0], [0, 1], [-1, 0], [0, -1]]

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    curr_y, curr_x = 0, 0
    min_y, max_y = 0, 0
    min_x, max_x = 0, 0
    rotate = 0
    for i in s:
        if i == "R":
            rotate = (rotate + 1) % 4
        elif i == "L":
            rotate = (rotate + 3) % 4
        elif i == "F":
            curr_y += v[rotate][0]
            curr_x += v[rotate][1]
        elif i == "B":
            curr_y -= v[rotate][0]
            curr_x -= v[rotate][1]

        min_y = min(min_y, curr_y)
        min_x = min(min_x, curr_x)
        max_y = max(max_y, curr_y)
        max_x = max(max_x, curr_x)

    print((max_x - min_x) * (max_y - min_y))