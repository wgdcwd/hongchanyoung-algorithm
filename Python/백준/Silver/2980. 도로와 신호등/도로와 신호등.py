import sys
input = sys.stdin.readline

n, l = map(int, input().split())

blinkers = []
for _ in range(n):
    blinkers.append(list(map(int, input().split())))

time = 0
curr_pos = 0
for pos, red, green in blinkers:
    time += pos - curr_pos
    curr_pos = pos
    temp = time % (red + green)
    if temp < red:
        time += red - temp

time += l - blinkers[-1][0]
print(time)