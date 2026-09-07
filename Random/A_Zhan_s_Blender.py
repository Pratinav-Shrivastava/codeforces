T = int(input())

for _ in range(T):
    n = int(input())
    x, y = map(int, input().split())
    x = min(x, y)
    print((n + x - 1) // x)
