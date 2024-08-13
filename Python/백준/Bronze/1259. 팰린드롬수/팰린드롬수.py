while True:
    i = input()
    if i == "0":
        break
    print("yes" if i == i[::-1] else "no")