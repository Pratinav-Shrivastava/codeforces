k, r = map(int, input().split())
for t in range(1, 11):
    if (k*t) % 10 in (0,r):
        print(t)
        break