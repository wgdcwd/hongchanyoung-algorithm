def solution(friends, gifts):
    #일단 선물 많이 받은애가 선물 적게받은애한테 선물줌
    #주고받은게 같다면 선물지수가 작은사람이 큰사람한테 선물줌
    #선물지수는 남에게 선물 많이줄수록 작아짐. 준 선물 - 받은 선물
    #a, b  = a가 b한테 선물줌
    gift_score = {}
    give_and_take = {}

    for person in friends:
        gift_score[person] = 0
        give_and_take[person] = {}

    for a in friends: #give_and_take[a][b] = a가 b에게 준 선물의 개수
        for b in friends:
            give_and_take[a][b] = 0
            give_and_take[b][a] = 0

    
    for a, b in [s.split() for s in gifts]:
        gift_score[a] += 1
        gift_score[b] -= 1
        give_and_take[a][b] += 1

    ans = {}
    for person in friends:
        ans[person] = 0
    #print(gift_score)
    #print(give_and_take)
    for a in friends:
        for b in friends:
            if give_and_take[a][b] > give_and_take[b][a]: #a가 b에게 준 선물이 b가 a에게 준 선물보다 많으면
                ans[a] += 1
            elif give_and_take[a][b] < give_and_take[b][a]:
                ans[b] += 1
            elif give_and_take[a][b] == give_and_take[b][a]:
                if gift_score[a] > gift_score[b]:
                    ans[a] += 1
                elif gift_score[a] < gift_score[b]:
                    ans[b] += 1
    
    return max(ans.values()) // 2