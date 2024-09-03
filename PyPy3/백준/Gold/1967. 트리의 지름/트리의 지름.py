import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
is_leaf = [True] * (n + 1)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
    is_leaf[u] = False

leaves = []
for i, x in enumerate(is_leaf):
    if x:
        leaves.append(i)

ans = [0]


def dfs(curr_point, curr_w, before):
    #print("D")
    ans[0] = max(ans[0], curr_w)

    for next_point, next_w in graph[curr_point]:
        if next_point == before:
            continue
        dfs(next_point, next_w + curr_w, curr_point)


for i in leaves[1:]:
    dfs(i, 0, 0)

print(ans[0])
