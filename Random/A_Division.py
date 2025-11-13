t = int(input())
for _ in range(t):
    r = int(input())
    div = 1 + (r < 1900) + (r < 1600) + (r < 1400)
    print(f"Division {div}")
