def solve():
    n = int(input())
    mp = {
        "00": 10**9,
        "01": 10**9,
        "10": 10**9,
        "11": 10**9
    }

    for _ in range(n):
        x, s = input().split()
        x = int(x)
        mp[s] = min(mp[s], x)

    ans = min(mp["11"], mp["10"] + mp["01"])

    if ans > 10**6:
        print(-1)
    else:
        print(ans)


t = int(input())
for _ in range(t):
    solve()