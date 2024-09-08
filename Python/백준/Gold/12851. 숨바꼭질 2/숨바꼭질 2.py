from collections import deque

n, k = map(int, input().split())
if n >= k:
    print(n - k)
    print(1)
    exit(0)

visited = [False] * (2 * k + 1)
q = deque()
q.append(n)
visited[n] = True
min_time = False
curr_time = 0
time_count = 1
next_time_count = 0

temp = set()

while True:
    curr_pos = q.popleft()
    temp.add(curr_pos)
    time_count -= 1
    if curr_pos == k:
        min_time = curr_time
        print(curr_time)
        break
    if curr_pos > 0:
        if not visited[curr_pos - 1]:
            q.append(curr_pos - 1)
            next_time_count += 1
    if curr_pos <= k:
        if not visited[curr_pos + 1]:
            q.append(curr_pos + 1)
            next_time_count += 1
        if not visited[curr_pos * 2]:
            q.append(curr_pos * 2)
            next_time_count += 1

    if time_count == 0:
        curr_time += 1
        time_count, next_time_count = next_time_count, 0
        for i in temp:
            visited[i] = True
        temp = set()


ans = 1
for _ in range(time_count):
    curr_pos = q.popleft()
    if curr_pos == k:
        ans += 1
        continue

print(ans)