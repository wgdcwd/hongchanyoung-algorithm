n = int(input())
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))

dp = [[0, 0, 0], [5000, costs[0][0] + costs[1][1], costs[0][0] + costs[1][2]]]
for i in range(2, n - 1):
    temp = [0, 0, 0]
    temp[0] = min(dp[-1][2], dp[-1][1]) + costs[i][0]
    temp[1] = min(dp[-1][2], dp[-1][0]) + costs[i][1]
    temp[2] = min(dp[-1][0], dp[-1][1]) + costs[i][2]
    dp.append(temp)

red = min(min(dp[-1][0], dp[-1][2]) + costs[-1][1], min(dp[-1][0], dp[-1][1]) + costs[-1][2])


dp = [[0, 0, 0], [costs[0][1] + costs[1][0], 5000, costs[0][1] + costs[1][2]]]
for i in range(2, n - 1):
    temp = [0, 0, 0]
    temp[0] = min(dp[-1][2], dp[-1][1]) + costs[i][0]
    temp[1] = min(dp[-1][2], dp[-1][0]) + costs[i][1]
    temp[2] = min(dp[-1][0], dp[-1][1]) + costs[i][2]
    dp.append(temp)

green = min(min(dp[-1][1], dp[-1][2]) + costs[-1][0], min(dp[-1][0], dp[-1][1]) + costs[-1][2])


dp = [[0, 0, 0], [costs[0][2] + costs[1][0], costs[0][2] + costs[1][1], 5000]]
for i in range(2, n - 1):
    temp = [0, 0, 0]
    temp[0] = min(dp[-1][2], dp[-1][1]) + costs[i][0]
    temp[1] = min(dp[-1][2], dp[-1][0]) + costs[i][1]
    temp[2] = min(dp[-1][0], dp[-1][1]) + costs[i][2]
    dp.append(temp)

blue = min(min(dp[-1][1], dp[-1][2]) + costs[-1][0], min(dp[-1][0], dp[-1][2]) + costs[-1][1])

print(min(red, green, blue))