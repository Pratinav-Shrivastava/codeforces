s = input()

current = 'a'
total_rotations = 0

for ch in s:
    diff = abs(ord(ch) - ord(current))
    total_rotations += min(diff, 26 - diff)
    current = ch

print(total_rotations)
