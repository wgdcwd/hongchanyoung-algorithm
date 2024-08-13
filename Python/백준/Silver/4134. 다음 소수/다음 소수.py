n = int(input())


def is_prime(x):
    if x == 1 or x == 0:
        return False
    if x <= 3:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for _ in range(n):
    number = int(input())
    while True:
        if is_prime(number):
            print(number)
            break
        number += 1
