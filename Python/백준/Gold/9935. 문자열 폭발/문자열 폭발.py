from collections import deque
s = input()
boom = list(input())
boom_last = boom[-1]
boom_len = len(boom)

stk = []

for i in range(len(s)):
    stk.append(s[i])
    if s[i] == boom_last:
        if stk[-boom_len:] == boom:
            for j in range(boom_len):
                stk.pop()

if stk:
    print(''.join(stk))
else:
    print("FRULA")