t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    used = [False] * n
    p = []

    for x in a:
        if not used[x - 1]:
            used[x - 1] = True
            p.append(x)

    print(*p)
