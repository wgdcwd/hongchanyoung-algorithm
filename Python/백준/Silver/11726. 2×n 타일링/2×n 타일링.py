import math
n = int(input())

case = []

for two in range(n // 2 + 1):
    case.append([two, n - 2 * two])

ans = 0
for a, b in case:
    ans += math.factorial(a + b) // (math.factorial(b) * math.factorial(a))

print(ans % 10007)