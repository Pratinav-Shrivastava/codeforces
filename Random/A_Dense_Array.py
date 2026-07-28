def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    last = arr[0]

    for i in range(1, n):
        nw = arr[i]
        a = min(last, nw)
        b = max(last, nw)

        while a * 2 < b:
            ans += 1
            a *= 2

        last = nw

    print(ans)


t = int(input())
for _ in range(t):
    solve()