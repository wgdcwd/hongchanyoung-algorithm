s = input()
arr = []
temp = []
for i in s:
    if i == "-" or i == "+":
        arr.append(int("".join(temp)))
        temp = []
        arr.append(i)
    else:
        temp.append(i)

arr.append(int("".join(temp)))

minus_switch = False

ans = 0
for i in arr:
    if i == "-":
        minus_switch = True
    elif i == "+":
        continue
    else:
        if minus_switch:
            ans -= int(i)
        else:
            ans += int(i)

print(ans)