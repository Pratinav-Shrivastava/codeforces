t = int(input())
magnets = []
for _ in range(t):
    magnets.append(input())

groups = 1
for i in range(1, len(magnets)):
    prev = magnets[i-1]
    curr = magnets[i]
    if curr == prev:
        continue
    else:
        groups += 1
print(groups)