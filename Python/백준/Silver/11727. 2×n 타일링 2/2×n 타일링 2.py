import math
n = int(input())
two = n // 2
ans = 0
while two >= 0:
    a = math.factorial(n - two)
    b = math.factorial(two) * math.factorial(n - 2 * two)
    ans += (a // b) * (2 ** two)
    two -= 1
print(ans % 10007)

