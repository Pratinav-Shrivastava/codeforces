s = input().strip()
t = input().strip()

pos = 0
for c in t:
    if s[pos] == c:
        pos += 1

print(pos + 1)