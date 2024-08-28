a = [c for c in input()]
b = [c for c in input()]

if len(a) > len(b): #간단히 a를 더 짧은 수열로 만듬
    a, b = b, a

lines = [[] for _ in a]

for a_idx, i in enumerate(a):
    for b_idx, j in enumerate(b):
        if i == j:
            lines[a_idx].append(b_idx)

#print(lines)

dp = [[0 for _ in range(len(b))] for _ in range(len(a) + 1)]
#dp[i][j] = a의 i번째 문자열까지 왔을때 b의 j번째 열까지의 LCS 길이

for i in range(len(a)):
    for line in lines[i]:
        if line == 0:
            dp[i + 1][line] = 1
        else:
            dp[i + 1][line] = dp[i][line - 1] + 1
    for j in range(len(b)):
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][max(0, j - 1)], dp[i + 1][j])
    #print(dp[i + 1])


print(max(dp[-1]))