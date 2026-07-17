def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    m = 0
    for i in range(0, n - 1, 2):
        m = max(m, abs(a[i] - a[i + 1]))

    print(m)


t = int(input())
for _ in range(t):
    solve()