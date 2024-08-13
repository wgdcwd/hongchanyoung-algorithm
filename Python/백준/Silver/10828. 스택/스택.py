import sys
n = int(input())
stk = []
for _ in range(n):
    i = sys.stdin.readline().strip()
    if i == "pop":
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif i == "size":
        print(len(stk))
    elif i == "empty":
        print(0 if stk else 1)
    elif i == "top":
        if stk:
            print(stk[-1])
        else:
            print(-1)
    else:
        temp, i = i.split()
        stk.append(i)