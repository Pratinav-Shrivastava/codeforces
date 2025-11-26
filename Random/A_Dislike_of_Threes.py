t = int(input())
for _ in range(t):
    k = int(input())
    cnt = 0
    n = 0
    while cnt < k:
        n += 1
        if n % 3 == 0 or n % 10 == 3:
            continue
        cnt += 1
    print(n)
