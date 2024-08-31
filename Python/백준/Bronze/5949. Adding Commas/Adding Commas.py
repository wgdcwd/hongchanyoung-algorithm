n = input()
n = [c for c in n]

cnt = 0
ans = []
while n:
    if cnt == 3:
        ans.append(",")
        cnt = 0
    ans.append(n.pop())
    cnt += 1
print("".join(ans[::-1]))