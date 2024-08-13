import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))
before = [i + 1 for i in range(n)] + [100001]
stk = [-1]
seq = []
ans = []
is_impossible = False
while len(seq) != n:
    # print("Before")
    # print(before)
    # print("stk")
    # print(stk)
    # print("seq")
    # print(seq)

    if stk[-1] == arr[0]:
        seq.append(stk.pop(-1))
        ans.append("-")
        arr.pop(0)
    elif arr[0] >= before[0]:
        stk.append(before.pop(0))
        ans.append("+")
    else:
        is_impossible = True
        break

if is_impossible:
    print("NO")
else:
    for i in ans:
        print(i)
