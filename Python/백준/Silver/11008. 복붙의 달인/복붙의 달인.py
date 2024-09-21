for _ in range(int(input())):
    s, c = input().split()
    i = 0
    time = 0
    while i < len(s):
        if s[i : i + len(c)] == c:
            i += len(c)
            time += 1
        else:
            i += 1
            time += 1

    print(time)