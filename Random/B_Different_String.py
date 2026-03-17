t = int(input())
for _ in range(t):
    s = input()
    if len(set(s)) == 1:
        print("NO")
    else:
        r = ''.join(sorted(s))
        if r == s:
            r = r[1:] + r[0]
        print("YES")
        print(r)