t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    ops = 0
    
    while max(a, b) <= n:
        if a < b:
            a += b
        else:
            b += a
        ops += 1
    
    print(ops)