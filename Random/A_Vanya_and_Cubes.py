n = int(input())

height = 0
used = 0

while True:
    next_level = (height + 1) * (height + 2) // 2
    if used + next_level > n:
        break
    used += next_level
    height += 1

print(height)
