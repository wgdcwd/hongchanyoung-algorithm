a = int(input())
b = int(input())
c = int(input())

n = str(a * b *c)
arr = [0] * 10
for c in n:
    arr[int(c)] += 1

for i in arr:
    print(i)