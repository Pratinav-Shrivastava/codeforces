n, ice_cream = map(int, input().split())
distressed = 0

for _ in range(n):
    op, d = input().split()
    d = int(d)
    if op == '+':
        ice_cream += d
    else:
        if ice_cream >= d:
            ice_cream -= d
        else:
            distressed += 1

print(ice_cream, distressed)