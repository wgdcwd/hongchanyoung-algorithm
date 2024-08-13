n = int(input())
s = set()
ans = 0
for _ in range(n):
    i = input()
    if i == "ENTER":
        s = set()
    else:
        if i in s:
            continue
        else:
            s.add(i)
            ans += 1

print(ans)