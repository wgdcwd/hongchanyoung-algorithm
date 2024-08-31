a = []
for _ in range(4):
    a.append(int(input()))
b = []
for _ in range(2):
    b.append(int(input()))

a.sort()

print(sum(a[1:]) + max(b))