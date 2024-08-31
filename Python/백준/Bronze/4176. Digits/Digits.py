while True:
    i = input()
    if i == "END":
        break

    cnt = 1
    while len(i) != int(i):
        cnt += 1
        i = str(len(i))
    print(cnt)