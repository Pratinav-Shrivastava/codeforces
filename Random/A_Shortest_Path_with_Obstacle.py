import sys

data = list(map(int, sys.stdin.read().split()))

t = data[0]
idx = 1

for _ in range(t):
    ax, ay = data[idx], data[idx + 1]
    bx, by = data[idx + 2], data[idx + 3]
    fx, fy = data[idx + 4], data[idx + 5]

    idx += 6

    ans = abs(ax - bx) + abs(ay - by)

    # F is directly between A and B on the same row/column.
    if ax == bx == fx and min(ay, by) < fy < max(ay, by):
        ans += 2

    elif ay == by == fy and min(ax, bx) < fx < max(ax, bx):
        ans += 2

    print(ans)