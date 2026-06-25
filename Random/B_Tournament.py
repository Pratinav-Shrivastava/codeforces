def solve():
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))

    mx = max(a)

    if k > 1 or a[j - 1] == mx:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()