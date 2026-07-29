t = int(input())

for _ in range(t):
    n = int(input())
    s = set()

    i = 1
    while i * i <= n:
        s.add(i * i)
        i += 1

    i = 1
    while i * i * i <= n:
        s.add(i * i * i)
        i += 1

    print(len(s))