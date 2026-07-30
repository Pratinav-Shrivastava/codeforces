def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    ans = 0
    cnt = 1

    for value in a:
        if value * cnt >= x:
            ans += 1
            cnt = 1
        else:
            cnt += 1

    print(ans)


t = int(input())
for _ in range(t):
    solve()