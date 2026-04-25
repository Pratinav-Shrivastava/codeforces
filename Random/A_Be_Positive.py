def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    k = 0
    for x in a:
        if x == 0:
            c += 1
        if x == -1:
            k += 1
    if k % 2 == 1:
        c += 2
    print(c)

t = int(input())
for _ in range(t):
    solve()