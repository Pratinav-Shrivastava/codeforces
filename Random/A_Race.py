def race(a, x, y):
    return("YES" if ((a<x) == (a<y)) else "NO")

t = int(input())
for _ in range(t):
    a, x, y, = map(int, input().split())
    print(race(a, x, y))
