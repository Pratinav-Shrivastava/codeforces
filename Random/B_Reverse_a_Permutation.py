t = int(input())

while t:
    t -= 1

    n = int(input())
    p = [0] + list(map(int, input().split()))

    ind = 1

    while ind <= n and p[ind] == n - ind + 1:
        ind += 1

    idx = -1

    for i in range(ind, n + 1):
        if p[i] == n - ind + 1:
            idx = i

    ans = []

    for i in range(1, ind):
        ans.append(p[i])

    if idx != -1:
        for i in range(idx, ind - 1, -1):
            ans.append(p[i])

        for i in range(idx + 1, n + 1):
            ans.append(p[i])

    print(*ans)
