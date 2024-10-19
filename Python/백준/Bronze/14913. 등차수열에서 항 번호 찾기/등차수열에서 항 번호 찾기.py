a, b, c = map(int, input().split())
if (c - a) % b == 0:
    ans = ((c - a) // b + 1)
    if ans < 1:
        print("X")
    else:
        print(ans)
else:
    print("X")