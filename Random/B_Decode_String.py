def get(i):
    return chr(ord('a') + i - 1)


def solve():
    n = int(input())
    s = input().strip()

    i = n - 1
    res = []

    while i >= 0:
        if s[i] != '0':
            res.append(get(int(s[i])))
            i -= 1
        else:
            res.append(get(int(s[i - 2:i])))
            i -= 3

    res.reverse()
    print(''.join(res))


t = int(input())
for _ in range(t):
    solve()