def solve():
    n = int(input())
    s = input()

    res = []

    i = 0
    while i < n:
        if s[i] == 'U':
            res.append('D')
        elif s[i] == 'D':
            res.append('U')
        else:
            res.append('LR')
            i += 1
        i += 1

    print(''.join(res))


t = int(input())

for _ in range(t):
    solve()
