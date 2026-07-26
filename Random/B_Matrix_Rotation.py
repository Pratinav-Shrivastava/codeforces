t = int(input())

for _ in range(t):
    a = [list(map(int, input().split())) for _ in range(2)]

    ok = False
    for _ in range(4):
        if (a[0][0] < a[0][1] and
            a[1][0] < a[1][1] and
            a[0][0] < a[1][0] and
            a[0][1] < a[1][1]):
            ok = True
            break

        # Rotate 90° clockwise
        a = [
            [a[1][0], a[0][0]],
            [a[1][1], a[0][1]]
        ]

    print("YES" if ok else "NO")