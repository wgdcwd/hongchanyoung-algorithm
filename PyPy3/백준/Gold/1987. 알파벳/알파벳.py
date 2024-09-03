import sys

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [[False] * (c + 2)]
for i in range(r):
    arr.append([False] + list(input().strip()) + [False])

arr.append([False] * (c + 2))

visited = [False] * 26
ans = [0]


def dfs(curr_r, curr_c, cnt):
    visited[ord(arr[curr_r][curr_c]) - ord('A')] = True
    ans[0] = max(ans[0], cnt + 1)
    next_point = [[curr_r - 1, curr_c], [curr_r + 1, curr_c], [curr_r, curr_c - 1], [curr_r, curr_c + 1]]
    for next_r, next_c in next_point:
        if not arr[next_r][next_c]:
            continue
        if visited[ord(arr[next_r][next_c]) - ord('A')]:
            continue
        dfs(next_r, next_c, cnt + 1)
    visited[ord(arr[curr_r][curr_c]) - ord('A')] = False

dfs(1, 1, 0)
print(ans[0])