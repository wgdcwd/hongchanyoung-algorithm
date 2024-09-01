from collections import deque
import sys
input = sys.stdin.readline

#사람수와 파티수 입력
n, m = map(int, input().split())

#진실을 알고있는 사람 입력
people = [False for _ in range(n + 1)]
for person in list(map(int, input().split()))[1:]:
    people[person] = True


#각 파티와 각 파티에 오는 사람 입력
parties = []
for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])

#각 사람이 어느 파티에 가는지 계산
people_and_party = [[]for _ in range(n + 1)]

for i, party in enumerate(parties):
    for person in party:
        people_and_party[person].append(i)


q = deque()
visited_person = [False for _ in range(n + 1)]
visited_party = [False for _ in range(m)]

for i, person in enumerate(people):
    if person:
        q.append(i)


while q:
    person = q.popleft()
    if visited_person[person]:
        continue
    visited_person[person] = True

    for party in people_and_party[person]:
        if not visited_party[party]:
            visited_party[party] = True
            for people_in_party in parties[party]:
                if not visited_person[people_in_party]:
                    q.append(people_in_party)

print(visited_party.count(False))