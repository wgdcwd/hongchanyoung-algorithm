alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input()
b = input()
s = []
for i in range(len(a)):
    s.append(a[i])
    s.append(b[i])

s = [alpha[ord(i) - ord("A")] for i in s]

while len(s) != 2:
    s = [(s[i] + s[i + 1]) % 10 for i in range(len(s) - 1)]

print(str(s[0]) + str(s[1]))