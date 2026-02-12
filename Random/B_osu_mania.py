t = int(input())
for _ in range(t):
    n = int(input())
    grid = [input() for _ in range(n)]

    result = []

    for row in reversed(grid):
        col = row.index("#") + 1
        result.append(str(col))

    print(*result)