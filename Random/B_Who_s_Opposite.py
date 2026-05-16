t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    n = 2 * abs(a - b)
    
    if max(a, b, c) > n:
        print(-1)
        continue
    
    d = c + n // 2
    if d > n:
        d -= n
    print(d)