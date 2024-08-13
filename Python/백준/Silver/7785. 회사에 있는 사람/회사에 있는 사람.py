import sys

input = sys.stdin.readline

n = int(input())
s = set()
for i in range(n):
    temp = input().split()
    if temp[1] == "enter":
        s.add(temp[0])
    else:
        s.remove(temp[0])

for people in sorted(s)[::-1]:
    print(people)