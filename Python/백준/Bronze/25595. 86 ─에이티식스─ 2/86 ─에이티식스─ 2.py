import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

start_pos = [-1, -1]
enemy_poses = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            start_pos = [i, j]
        elif arr[i][j] == 1:
            enemy_poses.append([i, j])

# print(start_pos)
# print(enemy_poses)

is_even = True if (start_pos[0] + start_pos[1]) % 2 == 0 else False

for i, j in enemy_poses:
    if is_even == ((i + j) % 2 == 0):
        print("Kiriya")
        exit(0)
print("Lena")