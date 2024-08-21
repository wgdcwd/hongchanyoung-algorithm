from collections import deque

n, m = map(int, input().split())

arr = [False for _ in range(101)]
jump_tile = []
jump_dict = {}
for _ in range(n + m):
    x, y = map(int, input().split())
    jump_tile.append(x)
    jump_dict[x] = y


#print(jump_dict)
#print(jump_tile)
q = deque()

q.append([1, 0])

while q:
    curr_pos, c = q.popleft()
    if curr_pos == 100:
        print(c)
        break
    if arr[curr_pos]:
        continue

    arr[curr_pos] = c
    if curr_pos in jump_tile:
        curr_pos = jump_dict[curr_pos]
        arr[curr_pos] = c

    for i in range(1, 7):
        if curr_pos + i > 100:
            continue
        if arr[curr_pos + i]:
            continue
        q.append([curr_pos + i, c + 1])
