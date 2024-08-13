import math
t = int(input())

for _ in range(t):
    n = int(input())
    case = []
    for three in range(n // 3 + 1):
        for two in range((n - 3 * three) // 2 + 1):
            case.append([three, two, n - 3 * three - 2 * two])

    ans = 0
    for a,b,c in case:
        ans += math.factorial(a + b + c) // (math.factorial(a) * math.factorial(b) * math.factorial(c))
    print(ans)