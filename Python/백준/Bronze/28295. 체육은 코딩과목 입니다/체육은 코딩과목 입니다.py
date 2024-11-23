d = 0

for i in range(10):
    o = int(input())
    if o == 1:
        d = (d + 1) % 4
    elif o == 2:
        d = (d + 2) % 4
    elif o == 3:
        d = (d + 3) % 4

if d == 0:
    print("N")
elif d == 1:
    print("E")
elif d == 2:
    print("S")
elif d == 3:
    print("W")