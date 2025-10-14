num = int(input())
i = 1
ans = ""
while i <= num:
    if i & 1:
        ans += "I hate "
    else:
        ans += "I love "
    if i != num:
        ans += "that "
    i += 1
ans += "it"
print(ans)
