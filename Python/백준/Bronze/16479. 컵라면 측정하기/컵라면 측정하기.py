k = int(input())
m1, m2 = map(int, input().split())

if m1 == m2:
    print(k * k)
else:
    print(k ** 2 - (abs(m1 - m2) / 2) ** 2)