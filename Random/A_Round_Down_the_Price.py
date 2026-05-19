def solve():
    m = int(input())
    t = str(m)
    s = "1" + "0" * (len(t) - 1)
    k = int(s)
    print(m - k)

t = int(input())
for _ in range(t):
    solve()