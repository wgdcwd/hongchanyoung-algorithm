import sys
input = sys.stdin.readline

stk = []
ans = 0
stk.append([0, 1000000, 0]) # [과제점수, 과제를 완료하기 위한 시간, 과제한 시간]
for _ in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        stk.append([temp[1], temp[2], 0])

    stk[-1][2] += 1
    if stk[-1][2] == stk[-1][1]:
        ans += stk[-1][0]
        stk.pop()

print(ans)