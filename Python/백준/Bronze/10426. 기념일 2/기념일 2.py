date, count = input().split()
count = int(count)
year, month, day = map(int, date.split("-"))
# print(year, month, day)

cnt = [0, 31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while count != 1:
    day += 1
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day > cnt[2][1]:
                day = 1
                month += 1
        else :
            if day > cnt[2][0]:
                day = 1
                month += 1
    else:
        if day > cnt[month]:
            day = 1
            month += 1

    if month == 13:
        year += 1
        month = 1

    count -= 1

if month // 10 == 0:
    month = '0' + str(month)
if day // 10 == 0:
    day = '0' + str(day)
print(f'{year}-{month}-{day}')