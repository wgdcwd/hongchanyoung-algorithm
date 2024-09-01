import sys

input = sys.stdin.readline

days, money = map(int, input().split())

my_coins = 0

coin_price = [int(input()) for _ in range(days)] +[0]

for i in range(days):

    if coin_price[i] < coin_price[i + 1]:
        my_coins += money // coin_price[i]
        money = money % coin_price[i]
    elif coin_price[i] > coin_price[i + 1]:
        money += coin_price[i] * my_coins
        my_coins = 0

print(money)