def solve():
    n = int(input())
    v = list(map(int, input().split()))
    maxPos = v.index(max(v))
    minPos = v.index(min(v))
    print(min(
        max(maxPos, minPos) + 1,
        (n - 1) - min(maxPos, minPos) + 1,
        (n - 1) - maxPos + minPos + 2,
        (n - 1) - minPos + maxPos + 2
    ))

t = int(input())
for _ in range(t):
    solve()