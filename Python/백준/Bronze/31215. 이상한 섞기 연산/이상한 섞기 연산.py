import sys
#input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    n = int(input())
    if n < 3:
        ans.append(1)
        continue
    for i in range(2, n + 1):
        if i % 2 != 0:
            ans.append(i)
            break

for i in ans:
    print(i)