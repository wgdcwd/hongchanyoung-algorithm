n = int(input())

#루트값이 정수인 애들의 개수
i = 1
while i * i <= n:
    i += 1

print(i - 1)