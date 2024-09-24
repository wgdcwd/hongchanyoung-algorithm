arr = list(map(int, input().split()))

i = 1
while True:
    c = 0
    for j in arr:
        if  i % j == 0:
            c += 1
    if c >= 3:
        print(i)
        exit(0)
    i += 1