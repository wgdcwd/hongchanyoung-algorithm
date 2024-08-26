import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

child = {}

for _ in range(n):
    parent, left, right = input().split()
    child[parent] = [left, right]

q = deque()
q.append("A")
ans = []
while q:
    curr = q.pop()
    ans.append(curr)
    l, r = child[curr]
    if r != ".":
        q.append(r)
    if l != ".":
        q.append(l)


print("".join(ans))

def inorder(curr):
    l, r = child[curr]
    if l != ".":
        inorder(l)
    print(curr, end="")
    if r != ".":
        inorder(r)


def postorder(curr):
    l, r = child[curr]
    if l != ".":
        postorder(l)
    if r != ".":
        postorder(r)
    print(curr, end="")


inorder("A")
print()
postorder("A")