import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, o, b, e, r = input().split()
    a = int(a)
    b = int(b)
    r = int(r)
    ans = 0
    if o == "*":
        ans = ((a * b) == r)
    elif o =="+":
        ans = ((a + b) == r)
    elif o == "-":
        ans = ((a - b) == r)
    elif o =="/":
        ans =((a / b) == r)
    print("correct" if ans else "wrong answer")