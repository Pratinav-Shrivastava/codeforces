def solve():
    n = int(input())
    print(*range(2, n + 1), 1)


t = int(input())
for _ in range(t):
    solve()