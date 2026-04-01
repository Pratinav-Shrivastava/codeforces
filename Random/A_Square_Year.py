t = int(input())
for _ in range(t):
    s = input().strip()
    n = int(s)
    k = int(n**0.5)
    if k * k == n:
        print(0, k)
    else:
        print(-1)