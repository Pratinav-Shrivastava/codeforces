t = int(input())

while t:
    l = list(map(int, input().split()))
    ok = False

    for i in range(3):
        if l[i] == l[(i + 1) % 3] + l[(i + 2) % 3]:
            ok = True

    for i in range(3):
        if l[i] % 2 == 0 and l[(i + 1) % 3] == l[(i + 2) % 3]:
            ok = True

    print("YES" if ok else "NO")
    t -= 1
