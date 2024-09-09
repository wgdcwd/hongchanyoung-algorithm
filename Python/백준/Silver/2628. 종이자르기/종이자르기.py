import sys

input = sys.stdin.readline

w, h = map(int, input().split())
m = int(input())

cut_w, cut_h = [], []
for _ in range(m):
    a, b = map(int, input().split())
    if a == 0:
        cut_w.append(b)
    else:
        cut_h.append(b)

cut_w = [0] + sorted(cut_w) + [h]
cut_h = [0] + sorted(cut_h) + [w]

# print(cut_w)
# print(cut_h)

cut_w = [cut_w[i] - cut_w[i - 1] for i in range(1, len(cut_w))]
cut_h = [cut_h[i] - cut_h[i - 1] for i in range(1, len(cut_h))]

# print(cut_w)
# print(cut_h)

print(max(cut_w) * max(cut_h))