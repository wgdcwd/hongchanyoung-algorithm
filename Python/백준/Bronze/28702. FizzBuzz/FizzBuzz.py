a = input()
b = input()
c = input()
ans = 0
if a.isdigit():
    ans = int(a) + 3
elif b.isdigit():
    ans = int(b) + 2
elif c.isdigit():
    ans = int(c) + 1

if ans % 3 == 0 and ans % 5 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else:
    print(ans)