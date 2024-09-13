n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

cnt_a = [[] for _ in range(101)]
cnt_b = [[] for _ in range(101)]
for i, j in enumerate(a):
    cnt_a[j].append(i)
for i, j in enumerate(b):
    cnt_b[j].append(i)

# print(cnt_a)
# print(cnt_b)
ans = []
end_a = -1
end_b = -1
for i in range(100, 0, -1):
    if not (cnt_a[i]) or (not cnt_b[i]):
        continue

    can_start_a = -1
    can_start_b = -1
    for idx, pos in enumerate(cnt_a[i]):
        if pos > end_a:
            can_start_a = idx
            break
    for idx, pos in enumerate(cnt_b[i]):
        if pos > end_b:
            can_start_b = idx
            break

    #print(i, can_start_a, can_start_b)
    if can_start_a == -1 or can_start_b == -1:
        continue

    append_cnt = min(len(cnt_a[i]) - can_start_a, len(cnt_b[i]) - can_start_b)
    for cnt in range(append_cnt):
        ans.append(i)

    end_a = cnt_a[i][can_start_a + append_cnt - 1]
    end_b = cnt_b[i][can_start_b + append_cnt - 1]

print(len(ans))
if ans:
    print(*ans)