import sys
from collections import deque

t = int(input())

for _ in range(t):
    func = sys.stdin.readline().strip()
    n = sys.stdin.readline().strip()
    n = int(n)
    arr = sys.stdin.readline().strip()[1:-1].split(",")
    if n < func.count("D"):
        print("error")
        continue

    front_start = 0
    back_end = n
    r_count = 0
    for i in func:
        if i == "R":
            r_count += 1
        elif i == "D":
            if r_count % 2 == 1:
                back_end -= 1
            else:
                front_start += 1

    is_reverse = -1 if r_count % 2 == 1 else 1
    #print(front_start, back_end)
    arr = arr[front_start:back_end][::is_reverse]
    arr = "[" + ','.join(arr) + "]"
    print(arr)