t = int(input())

for _ in range(t):
    s = int(input())
    result = ""

    for d in range(9, 0, -1):
        if s >= d:
            result = str(d) + result
            s -= d

    print(result)