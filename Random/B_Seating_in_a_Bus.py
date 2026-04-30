def solve():
    n = int(input())
    a = list(map(int, input().split()))
    left = a[0]
    right = a[0]
    for i in range(1, n):
        if a[i] + 1 == left:
            left = a[i]
        elif a[i] - 1 == right:
            right = a[i]
        else:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()