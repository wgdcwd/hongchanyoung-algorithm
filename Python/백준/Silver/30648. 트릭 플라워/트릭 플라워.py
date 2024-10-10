a, b = map(int, input().split())
r = int(input())

cnt =  [[0 for _ in range(r)] for _ in range(r)]
cnt[a][b] += 1
time = 0
while True:
    time += 1
    if a + b + 2 < r:
        a += 1
        b += 1
    else:
        a = a // 2
        b = b // 2

    cnt[a][b] += 1
    if cnt[a][b] == 2:
        break

print(time)