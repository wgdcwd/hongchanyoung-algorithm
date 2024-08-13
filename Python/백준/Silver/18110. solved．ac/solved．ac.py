import sys

n = int(input())
if n == 0:
    print(0)
    exit(0)


def cal(i):
    fst = (int(i * 10)) % 10
    i = i + (1 if fst >= 5 else 0)
    return int(i)


arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

cut = cal(n * 0.15)
arr = sorted(arr)
arr = arr[cut:n - cut]
print(cal(sum(arr) / len(arr)))
