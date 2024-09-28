s = input()
s = list(s)


def div_bracket(part):
    i = 0
    l = len(part)

    bracket_cnt = 0
    bracket_part = []
    temp = []
    while i < l:
        if part[i] == "(":
            bracket_cnt += 1
            bracket_part.append(part[i])
        elif part[i] == ")":
            bracket_cnt -= 1
            bracket_part.append(part[i])

            if bracket_cnt == 0:
                temp.append(bracket_part[1:-1])
                bracket_part = []
        else:
            if bracket_cnt > 0:
                bracket_part.append(part[i])
            else:
                temp.append(part[i])
        i += 1
    if bracket_part:
        temp.append(bracket_part[1:-1])
    return temp


def recur(part):
    part = div_bracket(part)
    for i in range(len(part)):
        if len(part[i]) != 1:
            part[i] = recur(part[i])
    return cal(cal(part, ["/", "*"]), ["-", "+"])[0]


def cal(part, targets):
    temp = []
    l = len(part)
    i = 1
    while i < l:
        if part[i] in targets:
            part[i + 1] = part[i - 1] + part[i + 1] + part[i]
        else:
            temp.append(part[i - 1])
            temp.append(part[i])
        i += 2
    temp.append(part[-1])
    return temp


s = recur(s)
print(s)
