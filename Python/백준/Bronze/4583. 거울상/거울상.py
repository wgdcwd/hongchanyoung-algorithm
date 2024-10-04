mirror_words = ['b', 'd', 'p', 'q', 'i', 'o', 'v', 'w', 'x']

while True:
    s = input()
    if s == "#":
        break
    can_trans = True
    for i in s:
        if not (i in mirror_words):
            can_trans = False
            break

    if can_trans:
        for i in s[::-1]:
            if i == 'b':
                print('d', end='')
            elif i == 'd':
                print('b', end='')
            elif i == 'p':
                print('q', end='')
            elif i == 'q':
                print('p', end='')
            else:
                print(i, end='')
        print()
    else:
        print("INVALID")