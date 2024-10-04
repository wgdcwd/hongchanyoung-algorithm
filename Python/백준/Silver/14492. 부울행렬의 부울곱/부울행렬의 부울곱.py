import sys
input = sys.stdin.readline
n = int(input())

a = []
b = []

for _ in range(n):
    temp = input().split()
    a.append([True if i == '1' else False for i in temp])

for _ in range(n):
    temp = input().split()
    b.append([True if i == '1' else False for i in temp])



def is_Ture(i, j):
    for k in range(n):
        if a[i][k] and b[k][j]:
            return True

    return False

ans = 0

for i in range(n):
    for j in range(n):
        if is_Ture(i, j):
            ans += 1

print(ans)