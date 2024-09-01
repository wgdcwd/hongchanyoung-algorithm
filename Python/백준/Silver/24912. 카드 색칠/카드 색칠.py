import sys

sys.setrecursionlimit(2000000)

n = int(input())
arr = [-1] + list(map(int, input().split())) + [-1]

for i in range(1, n + 1):
    if arr[i] != 0:
        if arr[i] == arr[i - 1]:
            print(-1)
            exit(0)

zero_place = []

for i in range(1, n + 1):
    if arr[i] != 0:
        if arr[i - 1] == 0:
            zero_place.append(i)
    else:
        if arr[i - 1] != 0:
            zero_place.append(i - 1)

if len(zero_place) % 2 == 1:
    zero_place.append(n + 1)

zero_place = [[zero_place[i], zero_place[i + 1]] for i in range(0, len(zero_place), 2)]


def set_colors(left, right):
    not_ends = [1, 2, 3]
    if arr[left] in not_ends:
        not_ends.remove(arr[left])
    if arr[right] in not_ends:
        not_ends.remove(arr[right])

    if right - left - 1 == 1:
        arr[left + 1] = not_ends[0]
    elif right - left - 1 == 2:
        if arr[left] == arr[right]:
            arr[left + 1] = not_ends[0]
            arr[left + 2] = not_ends[1]
        else:
            arr[left + 1] = not_ends[0]
            arr[left + 2] = not_ends[1]
    else:
        arr[left + 1] = not_ends[0]
        arr[right - 1] = not_ends[0]

        recur_color = [1, 2, 3]
        recur_color.remove(not_ends[0])
        for idx in range(left + 2, right - 1):
            arr[idx] = recur_color[0] if idx % 2 == 0 else recur_color[1]


#print(zero_place)
arr[0] = 1
arr[n + 1] = 1
for a, b in zero_place:
    set_colors(a, b)

print(*arr[1:n + 1])
