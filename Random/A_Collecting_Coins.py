t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    most = max(a, b, c)
    needed = (most - a) + (most - b) + (most - c)

    print("YES" if (needed <= n and (n-needed) % 3 == 0) else "NO")