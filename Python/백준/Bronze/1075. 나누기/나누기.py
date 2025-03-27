n = int(input())
f = int(input())
n = (n // 100) * 100
t = n % f
if t == 0:
    print("00")
else:
    if f - t > 0 and f - t < 10:
        print("0" + str(f - t))
    else:
        print(f - t)