n, h = map(int, input().split())
heights = list(map(int, input().split()))

for height in heights:
    if height > h:
        n += 1
print(n)