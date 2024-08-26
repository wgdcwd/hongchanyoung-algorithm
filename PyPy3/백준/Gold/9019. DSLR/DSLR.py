import sys
from collections import deque

def func_D(n):
    return (n * 2) % 10000


def func_S(n):
    return (n + 9999) % 10000


def func_L(n):
    return (n * 10 + (n // 1000)) % 10000


def func_R(n):
    return (n // 10) + 1000 * (n % 10)


t = int(input())
for _ in range(t):
    s, e = map(int, input().split())
    visited = [False for _ in range(10000)]
    q = deque()
    q.append([s, [None, None]])
    while q:
        p, fs = q.popleft()
        if visited[p]:
            continue
        visited[p] = fs
        if p == e:
            break
        temp = func_D(p)
        if not visited[temp]:
            q.append([temp, [p, "D"]])
        temp = func_S(p)
        if not visited[temp]:
            q.append([temp, [p, "S"]])
        temp = func_L(p)
        if not visited[temp]:
            q.append([temp, [p, "L"]])
        temp = func_R(p)
        if not visited[temp]:
            q.append([temp, [p, "R"]])

    ans = []
    q = deque()
    q.append(e)
    while q:
        curr = q.popleft()
        before, fs = visited[curr]
        if before == None:
            break
        ans.append(fs)
        q.append(before)
    
    print("".join(ans[::-1]))
            

