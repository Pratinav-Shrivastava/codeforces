def solve():
    n, k = map(int, input().split())
    a = list(range(n, 0, -1))
    a[n - k - 1:] = reversed(a[n - k - 1:])
    print(*a)

t = int(input())
for _ in range(t):
    solve()