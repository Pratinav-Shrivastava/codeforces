q = int(input())

for _ in range(q):
    n, m = map(int, input().split())
    carpet = [input().strip() for _ in range(n)]

    vika = "vika"
    fnd = 0

    for i in range(m):
        check = False
        for j in range(n):
            if carpet[j][i] == vika[fnd]:
                check = True

        if check:
            fnd += 1
            if fnd == 4:
                break

    print("YES" if fnd == 4 else "NO")