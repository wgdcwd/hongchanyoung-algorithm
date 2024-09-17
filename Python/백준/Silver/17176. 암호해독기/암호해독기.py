n = int(input())
password = [0] * 53
for i in list(map(int, input().split())):
    password[i] += 1

decode = input()
for i in decode:
    if i == " ":
        password[0] -= 1
    elif ord("A") <= ord(i) <= ord("Z"):
        password[ord(i) - ord("A") + 1] -= 1
    elif ord("a") <= ord(i) <= ord("z"):
        password[ord(i) - ord("a") + 27] -= 1

for i in password:
    if i != 0:
        print("n")
        exit(0)

print("y")