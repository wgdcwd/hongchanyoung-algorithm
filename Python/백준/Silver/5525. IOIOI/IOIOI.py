n = int(input())
s = int(input())
arr = input() + "x"

len_arr = []

i = 0
while i <= s - 3:
    if arr[i] == "O":
        i += 1
        continue

    cnt = 0
    while True:
        if arr[i + 1] == "O" and arr[i + 2] == "I":
            i += 2
            cnt += 1
        else:
            len_arr.append(cnt)
            i += 1
            break

ans = 0
if not len_arr:
    print(0)
    exit(0)
for i in len_arr:
    ans += max(0, i - n + 1)
#print(len_arr)
print(ans)