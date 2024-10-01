candy, money = map(int, input().split())
money = 10 ** money

pay = (candy // money) * money + money

if pay - candy <= candy - pay + money:
    print(pay)
else:
    print(pay - money)