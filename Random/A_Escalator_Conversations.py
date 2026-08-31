def solve():
    n, m, k, H = map(int, input().split())
    heights = list(map(int, input().split()))

    ans = 0
    for x in heights:
        diff = abs(H - x)
        if x != H and diff % k == 0 and diff <= (m - 1) * k:
            ans += 1

    print(ans)


t = int(input())

for _ in range(t):
    solve()