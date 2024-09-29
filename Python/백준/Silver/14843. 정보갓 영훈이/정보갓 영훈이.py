import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(float, input().split())))

score = 0
for s, a, t, m in arr:
    score += s * (1 + 1 / a) * (1 + m / t) / 4

m = int(input())
scores = [[float(input()), 0] for _ in range(m)] + [[score, 1]]
scores = sorted(scores)[::-1]

cut = int((m + 1) * 0.15)
is_god = False
for i in range(cut):
    if scores[i][1] == 1:
        is_god = True
        break

if is_god:
    print(f'The total score of Younghoon "The God" is{score: .2f}.')
else:
    print(f"The total score of Younghoon is{score: .2f}.")