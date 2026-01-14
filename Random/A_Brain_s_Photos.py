n, m = map(int, input().split())

colored = False

for _ in range(n):
    row = input().split()
    for pixel in row:
        if pixel in {'C', 'M', 'Y'}:
            colored = True

print("#Color" if colored else "#Black&White")
