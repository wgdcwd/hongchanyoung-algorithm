import sys

input = sys.stdin.readline
alp = [0 for _ in range(26)]
for _ in range(int(input())):
    p = input().strip()
    a = ord('a')
    alp[ord(p[0]) - a] += 1

ans = 0
for i in range(26):
    if alp[i] >= 5:
        ans += 1
        print(chr(i + ord('a')), end="")

if ans == 0:
    print("PREDAJA")