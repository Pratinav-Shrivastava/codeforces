def solve():
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)

    if s % n != 0:
        print(-1)
        return

    avg = s // n
    res = sum(1 for x in a if x > avg)

    print(res)


t = int(input())
for _ in range(t):
    solve()