s = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]

ans = True

for _ in range(int(input())):
    i = input()
    if i not in s:
        ans = False
        break

print("No" if ans else "Yes")