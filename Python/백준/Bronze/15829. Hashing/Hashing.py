n = int(input())
arr = [ord(c) - ord('a') + 1 for c in input()]

s = 0
for i in range(len(arr)):
    s += arr[i] * 31 ** i

print(s % 1234567891)