def solve():
    n, m, x = map(int, input().split())
    x -= 1
    col = x // n
    row = x % n
    print(row * m + col + 1)


t = int(input())
for _ in range(t):
    solve()