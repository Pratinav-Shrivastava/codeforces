t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    i = 0
    res = []
    while i < n:
        start = i
        res.append(s[i])
        i += 1
        while s[i] != s[start]:
            i += 1
        i += 1
    print(''.join(res))