import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().strip()
    dec = [False] * 10
    for i in n:
        dec[int(i)] = True
    print(dec.count(True))
