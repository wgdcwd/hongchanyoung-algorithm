import sys
input = sys.stdin.readline

coding_difficulty = list(map(int, input().split()))

ans = 0

for _ in range(int(input())):
    team_score = 0

    for _ in range(3):
        skill_cnt = list(map(int, input().split()))
        for i in range(3):
            team_score += coding_difficulty[i] * skill_cnt[i]

    ans = max(ans, team_score)

print(ans)